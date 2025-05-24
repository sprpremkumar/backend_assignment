"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

from abc import ABC, abstractmethod


class BaseAuth(ABC):
    """
    Abstract base class for handling authentication mechanisms.
    Provides shared functionality for loading and saving OAuth tokens.
    """

    @abstractmethod
    def get_access_token(self) -> str:
        """
        Abstract method that must be implemented to return a valid access token.

        :return: A valid access token string.
        :rtype: str
        """
        pass
