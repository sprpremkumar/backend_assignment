"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

from typing import Dict, List, Optional
from base_db_client import BaseSqlDBClient
from constant import SqlStatement, EmailColumn


class EmailSqlDBClient(BaseSqlDBClient):
    def __init__(self, db_path: str = "emails.db", persistent: bool = False):
        """
        Initializes the Email DB client and ensures the emails table exists.
        """
        super().__init__(db_path=db_path, persistent=persistent)
        self._init_db()

    def _init_db(self) -> None:
        """
        Creates the emails table if it doesn't already exist.
        """
        with self._get_connection() as conn:
            conn.execute(SqlStatement.CREATE_TABLE_STATEMENT)

    def insert_email(self, email: Dict) -> None:
        """
        Inserts a single email record into the database.
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

    def insert_emails_batch(self, emails: List[Dict]) -> None:
        """
        Inserts multiple email records in a batch operation.
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

    def get_all_emails(self) -> List[Dict]:
        """
        Retrieves all email records from the database.
        """
        with self._get_connection() as conn:
            cursor = conn.execute(SqlStatement.LIST_STATEMENT)
            return [dict(row) for row in cursor.fetchall()]

    def get_email_by_id(self, email_id: str) -> Optional[Dict]:
        """
        Retrieves a single email record by ID.
        """
        with self._get_connection() as conn:
            cursor = conn.execute(SqlStatement.FETCH_BY_ID_STATEMENT, (email_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def update_email_fields(self, email_id: str, updates: Dict) -> None:
        """
        Updates specified fields for a given email ID.
        """
        if not updates:
            raise ValueError("No fields provided to update.")

        set_clause = ", ".join(f"{field} = ?" for field in updates)
        values = list(updates.values()) + [email_id]

        with self._get_connection() as conn:
            conn.execute(SqlStatement.UPDATE_STATEMENT.format(set_clause=set_clause), values)
