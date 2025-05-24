"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

import sqlite3
from typing import Optional


class BaseSqlDBClient:
    def __init__(self, db_path: str = "database.db", persistent: bool = False):
        """
        Initializes the base database client.

        :param db_path: Path to the SQLite database file.
        :param persistent: If True, keeps a persistent connection open.
        """
        self.db_path = db_path
        self.persistent = persistent
        self.conn: Optional[sqlite3.Connection] = None
        if self.persistent:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row

    def _get_connection(self) -> sqlite3.Connection:
        """
        Provides a SQLite connection.

        :return: SQLite connection object.
        """
        if self.persistent and self.conn:
            return self.conn
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def close(self) -> None:
        """
        Closes the persistent database connection if it exists.
        """
        if self.persistent and self.conn:
            self.conn.close()
            self.conn = None
