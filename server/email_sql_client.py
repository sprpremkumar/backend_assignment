"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

from constant import SqlStatement, EmailColumn, DBPath
from server.base_db_client import BaseSqlDBClient


class EmailSqlDBClient(BaseSqlDBClient):
    def __init__(self, db_path: str = DBPath.EMAILS, persistent: bool = False):
        """
        Initialize the Email DB client and ensure the emails table exists.

        :param str db_path: Path to the SQLite database file.
        :param bool persistent: Whether to keep the connection persistent.
        """
        super().__init__(db_path=db_path, persistent=persistent)
        self.__init_db()

    def __init_db(self) -> None:
        """
        Create the emails table if it doesn't already exist.

        :return: None
        """
        with self._get_connection() as conn:
            conn.execute(SqlStatement.CREATE_TABLE_STATEMENT)

    def insert_email(self, email: dict) -> None:
        """
        Insert a single email record into the database.

        :param dict email: Email data with keys matching EmailColumn attributes.
        :return: None
        """
        with self._get_connection() as conn:
            conn.execute(SqlStatement.INSERT_STATEMENT, (
                email[EmailColumn.ID],
                email[EmailColumn.FROM],
                email[EmailColumn.TO],
                email[EmailColumn.SUBJECT],
                email[EmailColumn.BODY],
                email[EmailColumn.RECEIVED_AT],
                email[EmailColumn.LABELS]
            ))

    def insert_emails_batch(self, emails: list) -> None:
        """
        Insert multiple email records into the database in a batch.

        :param list emails: List of email dictionaries.
        :return: None
        """
        with self._get_connection() as conn:
            conn.executemany(SqlStatement.INSERT_STATEMENT, [
                (
                    email[EmailColumn.ID],
                    email[EmailColumn.FROM],
                    email[EmailColumn.TO],
                    email[EmailColumn.SUBJECT],
                    email[EmailColumn.BODY],
                    email[EmailColumn.RECEIVED_AT],
                    email[EmailColumn.LABELS]
                ) for email in emails
            ])

    def get_all_emails(self) -> list:
        """
        Retrieve all email records from the database.

        :return: List of all emails.
        :rtype: list
        """
        with self._get_connection() as conn:
            cursor = conn.execute(SqlStatement.LIST_STATEMENT)
            return [dict(row) for row in cursor.fetchall()]

    def get_email_by_id(self, email_id: str) -> dict | None:
        """
        Retrieve a single email record by its ID.

        :param str email_id: ID of the email to fetch.
        :return: Email data if found, otherwise None.
        :rtype: dict | None
        """
        with self._get_connection() as conn:
            cursor = conn.execute(SqlStatement.FETCH_BY_ID_STATEMENT, (email_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def update_email_fields(self, email_id: str, updates: dict) -> None:
        """
        Update specific fields of an email record by its ID.

        :param str email_id: ID of the email to update.
        :param dict updates: Dictionary of fields and new values to update.
        :raises ValueError: If updates dictionary is empty.
        """
        if not updates:
            raise ValueError("No fields provided to update.")

        set_clause = ", ".join(f"{field} = ?" for field in updates)
        values = list(updates.values()) + [email_id]

        with self._get_connection() as conn:
            conn.execute(SqlStatement.UPDATE_STATEMENT.format(set_clause=set_clause), values)
