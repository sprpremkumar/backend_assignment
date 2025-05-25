"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""
from unittest.mock import Mock

from tests.mock import MESSAGE_MOCK


def mock_access_token(*args, **kwargs):
    return "access_token"


def mock_get_message_ids(*args, **kwargs):
    return ["19705b24f09c7f9e"]


def mock_get_message(*args, **kwargs):
    mock_response = Mock()
    mock_response.json.return_value = MESSAGE_MOCK
    return mock_response


def mock_get_messages(*args, **kwargs):
    mock_response = Mock()
    mock_response.json.return_value = {"messages": [MESSAGE_MOCK]}
    return mock_response


RULE_JSON = {
    "predicate": "All",
    "rules": [
        {
            "field": "to",
            "predicate": "contains",
            "value": "sprpremkumar@gmail.com"
        }
    ],
    "actions": [
        {
            "type": "mark_as_read"
        },
        {
            "type": "move_message",
            "destination": "Processed"
        }
    ]
}
