"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

from datetime import datetime, timedelta

from dateutil import parser as dt_parser

from constant import EmailColumn, RuleProperty, Predicate, Field, ActionType, Labels, RequestParam
from server.email_sql_client import EmailSqlDBClient
from service.gmail_service import GmailService


class EmailRuleProcessor:
    """
    RuleEngine evaluates rules defined in a JSON structure and applies actions to emails.

    :param dict rule_json: Rule configuration containing predicates, rules, and actions
    """

    def __init__(self, rule_json: dict):
        self.predicate = rule_json.get(RuleProperty.PREDICATE, Predicate.ALL.title()).lower()
        self.rules = rule_json.get(RuleProperty.RULES, [])
        self.actions = rule_json.get(RuleProperty.ACTIONS, [])
        self.email_db_client = EmailSqlDBClient()
        self.gmail_service = GmailService()

    @staticmethod
    def __evaluate_string_field(predicate: str, email_value: str, value: str) -> bool:
        """
        Evaluate a string field based on the given predicate.

        :param str predicate: Type of predicate
        :param str email_value: Value from email
        :param str value: Expected value from rule
        :return: Result of predicate evaluation
        :rtype: bool
        """
        return {
            Predicate.CONTAINS: lambda: value in email_value,
            Predicate.DOES_NOT_CONTAINS: lambda: value not in email_value,
            Predicate.ANY: lambda: email_value == value,
            Predicate.DOES_NOT_EQUALS: lambda: email_value != value,
        }.get(predicate, lambda: False)()

    @staticmethod
    def __evaluate_date_field(predicate: str, email_value, value: str) -> bool:
        """
        Evaluate a date field based on the given predicate.

        :param str predicate: Type of predicate
        :param str|datetime email_value: Value from email (can be str or datetime)
        :param str value: Number of days in string form
        :return: Result of predicate evaluation
        :rtype: bool
        """
        if isinstance(email_value, str):
            email_value = dt_parser.parse(email_value)

        delta_days = timedelta(days=int(value))
        now = datetime.now()

        return {
            Predicate.LESS_THAN_DAYS: lambda: email_value > now - delta_days,
            Predicate.GREATER_THAN_DAYS: lambda: email_value < now - delta_days,
        }.get(predicate, lambda: False)()

    def _evaluate_condition(self, email: dict, condition: dict) -> bool:
        """
        Evaluate a single condition against a given email.

        :param dict email: Email data
        :param dict condition: Rule condition to evaluate
        :return: True if condition is satisfied, else False
        :rtype: bool
        """
        field = condition[RuleProperty.FIELD]
        predicate = condition[RuleProperty.PREDICATE].lower()
        value = condition[RuleProperty.VALUE].lower()
        email_value = email.get(field, "").lower()

        if field not in EmailColumn.SUPPORTED_FIELDS:
            raise ValueError(f"Field '{field}' is not supported.")

        if field in EmailColumn.STRING_FIELDS:
            return self.__evaluate_string_field(predicate, email_value, value)
        elif field in EmailColumn.DATE_FIELDS:
            return self.__evaluate_date_field(predicate, email_value, value)

        return False

    def evaluate_email(self, email: dict) -> bool:
        """
        Evaluate all rules against a single email.

        :param dict email: Email data to evaluate
        :return: True if email satisfies rules, else False
        :rtype: bool
        """
        results = [self._evaluate_condition(email, rule) for rule in self.rules]

        if self.predicate == Predicate.ALL:
            return all(results)
        elif self.predicate == Predicate.ANY:
            return any(results)

        return False

    def apply_actions(self, email: dict) -> None:
        """
        Apply configured actions to an email if it matches the rule.

        :param dict email: Email data to apply actions on
        """
        email_id = email[EmailColumn.ID]

        for action in self.actions:
            action_type = action[Field.TYPE]

            if action_type == ActionType.MARK_AS_READ:
                self.email_db_client.update_email_fields(email_id, {
                    EmailColumn.LABELS: Labels.READ.lower()
                })
                self.gmail_service.update_message(email_id, {
                    RequestParam.REMOVE_LABEL_IDS: [Labels.UNREAD]
                })

            elif action_type == ActionType.MARK_AS_UNREAD:
                self.email_db_client.update_email_fields(email_id, {
                    EmailColumn.LABELS: Labels.UNREAD.lower()
                })
                self.gmail_service.update_message(email_id, {
                    RequestParam.ADD_LABEL_IDS: [Labels.UNREAD]
                })

            elif action_type == ActionType.MOVE_MESSAGE:
                destination = action.get(Field.DESTINATION, "Default").lower()
                self.email_db_client.update_email_fields(email_id, {
                    EmailColumn.LABELS: destination
                })
                self.gmail_service.update_message(email_id, {
                    RequestParam.REMOVE_LABEL_IDS: [destination]
                })

    def process(self, emails: list[dict]) -> None:
        """
        Process a list of emails: evaluate each and apply actions if matched.

        :param list emails: List of email data dictionaries
        """
        for email in emails:
            if self.evaluate_email(email):
                self.apply_actions(email)
