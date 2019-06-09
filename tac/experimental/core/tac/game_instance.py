# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
import copy
import datetime
from enum import Enum
from typing import List, Optional, Set

from oef.query import Query
from oef.schema import Description

from tac.experimental.core.tac.dialogues import Dialogues
from tac.experimental.core.tac.lock_manager import LockManager
from tac.game import AgentState, WorldState, GameConfiguration
from tac.helpers.misc import build_query, get_goods_quantities_description, marginal_utility
from tac.protocol import GameData


class GamePhase(Enum):
    PRE_GAME = 'pre_game'
    GAME_SETUP = 'game_setup'
    GAME = 'game'
    POST_GAME = 'post_game'


class Search:

    def __init__(self):
        self.id = 0
        self.ids_for_tac = set()  # type: Set[int]
        self.ids_for_sellers = set()  # type: Set[int]
        self.ids_for_buyers = set()  # type: Set[int]

    def get_next_id(self) -> int:
        """
        Generates the next search id and stores it.

        :return: a search id
        """
        self.id += 1
        return self.id


class GameInstance:
    """
    The GameInstance maintains state of the game from the agent's perspective.
    """

    def __init__(self, agent_name: str, is_world_modeling: bool = False, services_interval: int = 10, register_as: str = 'both', search_for: str = 'both', pending_transaction_timeout: int = 10):
        self.agent_name = agent_name
        self.controller_pbk = None  # type: Optional[str]

        self._search = Search()
        self._dialogues = Dialogues()

        self._game_phase = GamePhase.PRE_GAME

        self._game_configuration = None  # type: Optional[GameConfiguration]
        self._initial_agent_state = None  # type: Optional[AgentState]
        self._agent_state = None  # type: Optional[AgentState]
        self._is_world_modeling = is_world_modeling
        self._world_state = None  # type: Optional[WorldState]

        self._services_interval = datetime.timedelta(0, services_interval)
        self._last_update_time = datetime.datetime.now() - self._services_interval
        self._last_search_time = datetime.datetime.now() - datetime.timedelta(0, round(services_interval / 2.0))

        self._register_as = register_as
        self._search_for = search_for

        self.goods_supplied_description = None
        self.goods_demanded_description = None

        self.lock_manager = LockManager(agent_name, pending_transaction_timeout=pending_transaction_timeout)
        self.lock_manager.start()

    def init(self, game_data: GameData):
        # populate data structures about the started competition
        self._game_configuration = GameConfiguration(game_data.nb_agents, game_data.nb_goods, game_data.tx_fee,
                                                     game_data.agent_pbks, game_data.agent_names, game_data.good_pbks)
        self._initial_agent_state = AgentState(game_data.money, game_data.endowment, game_data.utility_params)
        self._agent_state = AgentState(game_data.money, game_data.endowment, game_data.utility_params)
        if self.is_world_modeling:
            opponent_pbks = self.game_configuration.agent_pbks
            opponent_pbks.remove(game_data.public_key)
            self._world_state = WorldState(opponent_pbks, self.game_configuration.good_pbks, self.initial_agent_state)

    def reset(self):
        self.controller_pbk = None
        self._search = Search()
        self._dialogues = Dialogues()
        self._game_phase = GamePhase.PRE_GAME
        self._game_configuration = None
        self._initial_agent_state = None
        self._agent_state = None
        self._world_state = None
        self.goods_supplied_description = None
        self.goods_demanded_description = None

    @property
    def search(self) -> Search:
        return self._search

    @property
    def dialogues(self):
        return self._dialogues

    @property
    def game_phase(self):
        return self._game_phase

    @property
    def game_configuration(self):
        return self._game_configuration

    @property
    def initial_agent_state(self):
        return self._initial_agent_state

    @property
    def agent_state(self):
        return self._agent_state

    @property
    def world_state(self):
        return self._world_state

    @property
    def is_world_modeling(self):
        return self._is_world_modeling

    @property
    def services_interval(self):
        return self._services_interval

    @property
    def last_update_time(self):
        return self._last_update_time

    @property
    def last_search_time(self):
        return self._last_search_time

    @property
    def is_registering_as_seller(self):
        return self._register_as == 'seller' or self._register_as == 'both'

    @property
    def is_searching_for_sellers(self):
        return self._search_for == 'sellers' or self._search_for == 'both'

    @property
    def is_registering_as_buyer(self):
        return self._register_as == 'buyer' or self._register_as == 'both'

    @property
    def is_searching_for_buyers(self):
        return self._search_for == 'buyers' or self._search_for == 'both'

    def is_time_to_update_services(self) -> bool:
        """
        Checks if the agent should update the service directory.

        :return: bool indicating the action
        """
        now = datetime.datetime.now()
        result = now - self.last_update_time > self.services_interval
        if result:
            self._last_update_time = now
        return result

    def is_time_to_search_services(self) -> bool:
        """
        Checks if the agent should search the service directory.

        :return: bool indicating the action
        """
        now = datetime.datetime.now()
        result = now - self.last_search_time > self.services_interval
        if result:
            self._last_search_time = now
        return result

    def get_service_description(self, is_supply: bool) -> Description:
        """
        Get the description of
            - the supplied goods (as a seller), or
            - the demanded goods (as a buyer).

        :param is_supply: Boolean indicating whether it is supply or demand.

        :return: the description (to advertise on the Service Directory).
        """

        desc = get_goods_quantities_description(self.game_configuration.good_pbks,
                                                self.get_goods_quantities(is_supply),
                                                is_supply=is_supply)
        return desc

    def build_services_query(self, is_searching_for_sellers: bool) -> Optional[Query]:
        """
        Build the query to look for agents
            - which supply the agent's demanded goods (i.e. sellers), or
            - which demand the agent's supplied goods (i.e. buyers).

        :param is_searching_for_sellers: Boolean indicating whether the search is for sellers or buyers.

        :return: the Query, or None.
        """
        good_pbks = self.get_goods_pbks(is_supply=not is_searching_for_sellers)

        res = None if len(good_pbks) == 0 else build_query(good_pbks, is_searching_for_sellers)
        return res

    def get_goods_description(self, is_supply: bool) -> Description:
        """
        Get the description of
            - the supplied goods (as a seller), or
            - the demanded goods (as a buyer).

        :param is_supply: Boolean indicating whether it is supply or demand.

        :return: the description (to advertise on the Service Directory).
        """

        desc = get_goods_quantities_description(self.game_configuration.good_pbks,
                                                self.get_goods_quantities(is_supply),
                                                is_supply=is_supply)
        return desc

    def get_goods_pbks(self, is_supply: bool) -> Set[str]:
        """
        Wraps the function which determines supplied and demanded good pbks.

        :param is_supply: Boolean indicating whether it is referencing the supplied or demanded pbks.

        :return: a list of good pbks
        """
        state_after_locks = self.state_after_locks(is_seller=is_supply)
        pbks = BaselineStrategy.supplied_good_pbks(self.game_configuration.good_pbks, state_after_locks.current_holdings) if is_supply else BaselineStrategy.demanded_good_pbks(self.game_configuration.good_pbks, state_after_locks.current_holdings)
        return pbks

    def get_goods_quantities(self, is_supply: bool) -> List[int]:
        """
        Wraps the function which determines supplied and demanded good quantities.

        :param is_supply: Boolean indicating whether it is referencing the supplied or demanded quantities.

        :return: the vector of good quantities offered/requested.
        """
        state_after_locks = self.state_after_locks(is_seller=is_supply)
        quantities = BaselineStrategy.supplied_good_quantities(state_after_locks.current_holdings) if is_supply else BaselineStrategy.demanded_good_quantities(state_after_locks.current_holdings)
        return quantities

    def state_after_locks(self, is_seller: bool):
        """
        Apply all the locks to the current state of the agent. That is, assuming all
        the locked transactions will be successful.

        :param is_seller: Boolean indicating the role of the agent.

        :return: the agent state with the locks applied to current state
        """
        transactions = list(self.lock_manager.locks_as_seller.values()) if is_seller \
            else list(self.lock_manager.locks_as_buyer.values())
        state_after_locks = self._agent_state.apply(transactions, self.game_configuration.tx_fee)
        return state_after_locks


class BaselineStrategy:
    def supplied_good_quantities(current_holdings: List[int]) -> List[int]:
        """
        Generates list of quantities which are supplied.

        :param current_holdings: a list of current good holdings
        :return: a list of quantities
        """
        return [quantity - 1 for quantity in current_holdings]

    def supplied_good_pbks(good_pbks: List[str], current_holdings: List[int]) -> Set[str]:
        """
        Generates set of good pbks which are supplied.

        :param good_pbks: a list of good pbks
        :param current_holdings: a list of current good holdings
        :return: a set of pbks
        """
        return {good_pbk for good_pbk, quantity in zip(good_pbks, current_holdings) if quantity > 1}

    def demanded_good_quantities(current_holdings: List[int]) -> List[int]:
        """
        Generates list of quantities which are demanded.

        :param current_holdings: a list of current good holdings
        :return: a list of quantities
        """
        return [1 for _ in current_holdings]

    def demanded_good_pbks(good_pbks: List[str], current_holdings: List[int]) -> Set[str]:
        """
        Generates set of good pbks which are demanded.

        :param good_pbks: a list of good pbks
        :param current_holdings: a list of current good holdings
        :return: a set of pbks
        """
        return {good_pbk for good_pbk, quantity in zip(good_pbks, current_holdings)}

    def get_proposals(good_pbks: List[str], current_holdings: List[int], utility_params: List[int], tx_fee: float, is_seller: bool, is_world_modeling: bool, world_state: WorldState) -> List[Description]:
        """
        Generates proposals from the seller/buyer.

        :param good_pbks: a list of good pbks
        :param current_holdings: a list of current good holdings
        :param utility_params: a list of utility params
        :param tx_fee: the transaction fee
        :param is_seller: Boolean indicating the role of the agent

        :return: a list of proposals in Description form
        """
        quantities = BaselineStrategy.supplied_good_quantities(current_holdings) if is_seller else BaselineStrategy.demanded_good_quantities(current_holdings)
        proposals = []
        zeroslist = [0] * len(quantities)
        rounding_adjustment = 0.01
        for good_id, good_pbk in zip(range(len(quantities)), good_pbks):
            if is_seller and quantities[good_id] == 0: continue
            lis = copy.deepcopy(zeroslist)
            lis[good_id] = 1
            desc = get_goods_quantities_description(good_pbks, lis, is_supply=is_seller)
            delta_holdings = [i * -1 for i in lis] if is_seller else lis
            switch = -1 if is_seller else 1
            marginal_utility_from_single_good = marginal_utility(utility_params, current_holdings, delta_holdings) * switch
            share_of_tx_fee = round(tx_fee / 2.0, 2)
            if is_world_modeling:
                desc.values["price"] = world_state.expected_price(good_pbk, round(marginal_utility_from_single_good, 2), is_seller, share_of_tx_fee)
            else:
                if is_seller:
                    desc.values["price"] = round(marginal_utility_from_single_good, 2) + share_of_tx_fee + rounding_adjustment
                else:
                    desc.values["price"] = round(marginal_utility_from_single_good, 2) - share_of_tx_fee - rounding_adjustment
            proposals.append(desc)
        return proposals
