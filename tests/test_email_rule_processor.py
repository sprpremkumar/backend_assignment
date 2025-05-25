"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

import unittest
from copy import deepcopy

from engine.email_rule_processor import EmailRuleProcessor
from server.email_sql_client import EmailSqlDBClient
from tests import RULE_JSON


class TestEmailRuleProcessor(unittest.TestCase):

    def test_process(self):
        rule_processor = EmailRuleProcessor(RULE_JSON)
        db_client = EmailSqlDBClient()
        emails = [
            {
                'id': '19705b24f09c7f9e',
                'subject': 'Security alert',
                'from': 'Google <no-reply@accounts.google.com>',
                'to': 'sprpremkumar@gmail.com',
                'body': '[image: Google]\r\nCalendar App was granted access to your Google Account',
                'received_at': "datetime.datetime(2025, 5, 25, 9, 57, 40)",
                'labels': 'UNREAD,CATEGORY_UPDATES,INBOX'
            }
        ]
        db_client.insert_email(emails[0])
        rule_processor.process(emails)
        email_dict = db_client.get_email_by_id('19705b24f09c7f9e')
        self.assertEqual(email_dict['labels'], RULE_JSON["actions"][1]["destination"].lower(), "labels mismatch")


    def test_process_neg(self):
        rule_json = deepcopy(RULE_JSON)
        rule_json["rules"][0]["field"] = "Sender"
        rule_processor = EmailRuleProcessor(rule_json)
        emails = [
            {
                'id': '19705b24f09c7f9e',
                'subject': 'Security alert',
                'from': 'Google <no-reply@accounts.google.com>',
                'to': 'sprpremkumar@gmail.com',
                'body': '[image: Google]\r\nCalendar App was granted access to your Google Account',
                'received_at': "datetime.datetime(2025, 5, 25, 9, 57, 40)",
                'labels': 'UNREAD,CATEGORY_UPDATES,INBOX'
            }
        ]
        self.assertRaises(ValueError, rule_processor.process, emails)
