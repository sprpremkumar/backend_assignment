"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM

Main execution script to:
1. Fetch emails from Gmail using GmailService.
2. Store them in SQLite using EmailSqlDBClient.
3. Process rules loaded from a JSON file using EmailRuleProcessor.
"""

import json
from engine.email_rule_processor import EmailRuleProcessor
from server.email_sql_client import EmailSqlDBClient
from service.gmail_service import GmailService

# Instantiate shared services
_gmail_service = GmailService()
_email_db_client = EmailSqlDBClient()


def __insert_gmail_to_db() -> None:
    """
    Fetches messages from Gmail and inserts them into the local database.

    :return: None
    """
    gmail_messages = _gmail_service.get_messages()
    _email_db_client.insert_emails_batch(gmail_messages)


def __load_rule_json_file(path: str = "rules.json") -> dict:
    """
    Loads the rule configuration from a JSON file.

    :param str path: Path to the rules JSON file.
    :return: Dictionary representing the rule configuration.
    :rtype: dict
    """
    with open(path, "r") as json_file:
        return json.load(json_file)


def __process_rules(rule_json: dict) -> None:
    """
    Processes emails in the database against the provided rule JSON.

    :param dict rule_json: Rule definition loaded from JSON.
    :return: None
    """
    stored_emails = _email_db_client.get_all_emails()
    EmailRuleProcessor(rule_json).process(stored_emails)


def main() -> None:
    """
    Main execution entrypoint to:
    - Fetch emails from Gmail
    - Store them in the database
    - Process rule-based actions

    :return: None
    """
    __insert_gmail_to_db()
    rule_json = __load_rule_json_file()
    __process_rules(rule_json)


if __name__ == "__main__":
    main()
