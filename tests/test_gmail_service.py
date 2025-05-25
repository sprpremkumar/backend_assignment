"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""
import unittest
from unittest.mock import patch

from constant import RequestParam, Labels
from service.gmail_service import GmailService
from tests import mock_access_token, mock_get_message, mock_get_message_ids, mock_get_messages


class TestGmailService(unittest.TestCase):

    @patch("service.gmail_service.requests.get", mock_get_message)
    @patch("service.gmail_service.GmailService._GmailService__get_message_ids", mock_get_message_ids)
    @patch("service.gmail_service.OAuth2Auth.get_access_token", mock_access_token)
    def test_get_messages(self):
        gmail_service = GmailService()
        messages = gmail_service.get_messages()
        print(messages)
        self.assertEqual(len(messages), 1, "length mismatch")
        self.assertEqual(messages[0]['id'], "19705b24f09c7f9e", "id mismatch")

    @patch("service.gmail_service.requests.get", mock_get_messages)
    @patch("service.gmail_service.OAuth2Auth.get_access_token", mock_access_token)
    def test_get_message_ids(self):
        gmail_service = GmailService()
        messages = gmail_service._GmailService__get_message_ids()
        self.assertEqual(len(messages), 1, "length mismatch")
        self.assertEqual(messages[0], "19705b24f09c7f9e", "id mismatch")

    @patch("service.gmail_service.requests.request", mock_get_message)
    @patch("service.gmail_service.OAuth2Auth.get_access_token", mock_access_token)
    def test_update_message(self):
        gmail_service = GmailService()
        message = gmail_service.update_message("19705b24f09c7f9e",
                                                {RequestParam.ADD_LABEL_IDS: [Labels.UNREAD]})
        self.assertIn(Labels.UNREAD, message['labelIds'], "label not found")
