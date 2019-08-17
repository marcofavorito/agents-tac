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

"""This module contains the tests of the messages module."""
from tac.agents.v1.protocols.simple.serialization import SimpleSerializer

from tac.agents.v1.mail.messages import Message, SimpleMessage
from tac.agents.v1.mail.protocol import DefaultProtobufSerializer, DefaultJSONSerializer


def test_simple_serialization():
    """Test that the serialization for the 'simple' protocol."""
    msg = SimpleMessage(to="receiver", sender="sender", type=SimpleMessage.Type.BYTES, body=dict(content=b"hello"))
    msg_bytes = SimpleSerializer().encode(msg)
    actual_msg = SimpleSerializer().decode(msg_bytes)
    expected_msg = msg

    assert expected_msg == actual_msg


def test_default_json_serialization():
    """Test that the default json serialization works."""
    msg = Message(to="receiver", sender="sender", protocol_id="my_own_protocol", body={"content": "hello"})
    msg_bytes = DefaultJSONSerializer().encode(msg)
    actual_msg = DefaultJSONSerializer().decode(msg_bytes)
    expected_msg = msg

    assert expected_msg == actual_msg
