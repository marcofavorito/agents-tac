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
from abc import abstractmethod
from typing import Union

from oef.messages import CFP, Propose, Accept, Decline, Message as SimpleMessage, SearchResult, OEFErrorMessage, DialogueErrorMessage

from tac.experimental.core.tac.dialogues import Dialogue
from tac.protocol import Error, TransactionConfirmation, StateUpdate

AgentMessage = Union[SimpleMessage, CFP, Propose, Accept, Decline]


class ControllerReactionInterface:
    """
    This interface contains the methods to react to the ControllerAgent.
    """

    @abstractmethod
    def on_start(self) -> None:
        """
        On start of the competition, do the setup.

        :return: None
        """

    @abstractmethod
    def on_cancelled(self) -> None:
        """
        Handle the cancellation of the competition from the TAC controller.

        :return: None
        """

    @abstractmethod
    def on_transaction_confirmed(self, tx_confirmation: TransactionConfirmation) -> None:
        """
        On Transaction confirmed handler.

        :param tx_confirmation: the transaction confirmation

        :return: None
        """

    @abstractmethod
    def on_state_update(self, agent_state: StateUpdate) -> None:
        """
        On receiving the agent state update.

        :param agent_state: the current state of the agent in the competition.

        :return: None
        """

    @abstractmethod
    def on_tac_error(self, error: Error) -> None:
        """
        Handle error messages from the TAC controller.

        :return: None
        """


class ControllerActionInterface:
    """
    This interface contains the methods to interact with the ControllerAgent.
    """

    @abstractmethod
    def request_state_update(self) -> None:
        """
        Request a state update from the controller.
        """


class OEFSearchReactionInterface:
    """
    This interface contains the methods to react to the OEF.
    """

    @abstractmethod
    def on_search_result(self, search_result: SearchResult):
        """Handle search results."""

    @abstractmethod
    def on_oef_error(self, oef_error: OEFErrorMessage):
        """Handle an OEF error message."""

    @abstractmethod
    def on_dialogue_error(self, dialogue_error: DialogueErrorMessage):
        """Handler a dialogue error message"""


class OEFSearchActionInterface:
    """
    This interface contains the methods to interact with the OEF.
    """

    @abstractmethod
    def unregister_service(self) -> None:
        """Unregisters services to the OEF."""

    @abstractmethod
    def register_service(self) -> None:
        """Registers services to the OEF."""

    @abstractmethod
    def search_services(self) -> None:
        """Searches services on the OEF."""


class DialogueReactionInterface:
    """
    This interface contains the methods to maintain a Dialogue with other agents.
    """

    @abstractmethod
    def on_new_dialogue(self, msg: AgentMessage) -> Dialogue:
        """Given a new message, create a Dialogue object that specifies:
        - the protocol rules that messages must follow;
        - how the agent behaves in this dialogue.
        """

    @abstractmethod
    def on_existing_dialogue(self, msg: AgentMessage) -> Dialogue:
        """
        React to a message of an existing dialogue.
        """

    @abstractmethod
    def on_unidentified_dialogue(self, msg: AgentMessage) -> Dialogue:
        """
        React to a message of an unidentified dialogue.
        """


class DialogueActionInterface:
    """
    This interface contains the methods to maintain a Dialogue with other agents.
    """
