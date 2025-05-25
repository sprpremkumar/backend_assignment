"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""


class Scope:
    """
    OAuth2 scopes for accessing Gmail API.
    """
    GMAIL_READ_ONLY_SCOPE_CODE = 'https://www.googleapis.com/auth/gmail.readonly'
    GMAIL_MODIFY_SCOPE_CODE = 'https://www.googleapis.com/auth/gmail.modify'


class JsonFileName:
    """
    Filenames for OAuth2 credential and token storage.
    """
    CREDENTIALS = '/Users/premkumar/PycharmProjects/backend_assignment/config/credentials.json'
    TOKEN = '/Users/premkumar/PycharmProjects/backend_assignment/config/token.json'


class Operation:
    """
    File operation modes.
    """
    WRITE = 'w'


class Headers:
    """
    HTTP headers used in Gmail API requests.
    """
    AUTHORIZATION = 'Authorization'


class RequestParam:
    """
    Query parameters for Gmail API requests.
    """
    LABEL_IDS = 'labelIds'
    MAX_RESULTS = 'maxResults'
    INBOX = 'INBOX'
    ADD_LABEL_IDS = 'addLabelIds'
    REMOVE_LABEL_IDS = 'removeLabelIds'


class GmailResponse:
    """
    Keys expected in Gmail API response payloads.
    """
    MESSAGES = 'messages'
    ID = 'id'
    PARTS = 'parts'
    MIME_TYPE = 'mimeType'
    BODY = 'body'
    DATA = 'data'
    VALUE = 'value'
    NAME = 'name'
    PAYLOAD = 'payload'
    HEADERS = 'headers'
    FROM = 'From'
    TO = 'To'
    SUBJECT = 'Subject'
    INTERNAL_DATE = 'internalDate'
    LABEL_IDS = 'labelIds'


class MimeType:
    """
    MIME types used for email content.
    """
    PLAIN_TEXT = 'text/plain'


class Encoding:
    """
    Character encoding formats.
    """
    UTF = 'utf-8'


class HTTPMethod:
    """
    HTTP methods used for API calls.
    """
    POST = 'POST'


class GmailAPI:
    """
    Gmail API endpoint URLs.
    """
    LIST_MESSAGES = 'https://gmail.googleapis.com/gmail/v1/users/me/messages'
    MODIFY_MESSAGE = 'https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}/modify'


class EmailColumn:
    """
    Database column names for the emails table.
    """
    ID = 'id'
    FROM = 'from'
    TO = 'to'
    SUBJECT = 'subject'
    BODY = 'body'
    RECEIVED_AT = 'received_at'
    LABELS = 'labels'
    SUPPORTED_FIELDS = (ID, FROM, TO, SUBJECT, BODY, RECEIVED_AT, LABELS)
    STRING_FIELDS = (ID, FROM, TO, SUBJECT, BODY, LABELS)
    DATE_FIELDS = (RECEIVED_AT)


class SqlStatement:
    """
    SQL statements for managing the emails table.
    """
    CREATE_TABLE_STATEMENT = """
        CREATE TABLE IF NOT EXISTS emails (
            id TEXT PRIMARY KEY,
            "from" TEXT,
            "to" TEXT,
            subject TEXT,
            body TEXT,
            received_at INTEGER,
            labels TEXT
        )
    """
    INSERT_STATEMENT = """
        INSERT OR IGNORE INTO emails (id, "from", "to", subject, body, received_at, labels)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    LIST_STATEMENT = "SELECT * FROM emails"
    FETCH_BY_ID_STATEMENT = "SELECT * FROM emails WHERE id = ?"
    UPDATE_STATEMENT = "UPDATE emails SET {set_clause} WHERE id = ?"

class RuleProperty:
    """
    Defines keys used to describe rule properties for filtering or processing emails.
    """
    FIELD = 'field'
    PREDICATE = 'predicate'
    VALUE = 'value'
    RULES = 'rules'
    ACTIONS = 'actions'


class Predicate:
    """
    Defines supported conditional predicates for evaluating email rule criteria.
    """
    CONTAINS = 'contains'
    DOES_NOT_CONTAINS = 'does_not_contain'
    EQUALS = 'equals'
    DOES_NOT_EQUALS = 'does_not_equals'
    ALL = 'all'
    ANY = 'any'
    LESS_THAN_DAYS = 'less_than_days'
    GREATER_THAN_DAYS = 'greater_than_days'


class ActionType:
    """
    Defines possible actions that can be taken on an email when rule conditions are met.
    """
    MARK_AS_READ = 'mark_as_read'
    MARK_AS_UNREAD = 'mark_as_unread'
    MOVE_MESSAGE = 'move_message'


class Field:
    """
    Defines fields used in rule-based actions.
    """
    TYPE = 'type'
    DESTINATION = 'destination'

class Labels:
    """
    Gmail labels
    """
    READ = 'READ'
    UNREAD = 'UNREAD'

class DBPath:
    """
    DB path
    """
    DATABASE = 'database.db'
    EMAILS = 'emails.db'