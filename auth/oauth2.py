"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from auth.auth_base import BaseAuth
from constant import Scope, JsonFileName, Operation


class OAuth2Auth(BaseAuth):
    """
    Handles OAuth2 authentication using Google's InstalledAppFlow.
    Loads, saves, refreshes tokens, and initiates OAuth login when necessary.
    """

    def __init__(self):
        """
        Initializes the OAuth2 authentication handler.
        """
        super().__init__()
        self.credentials_path = JsonFileName.CREDENTIALS
        self.token_path = JsonFileName.TOKEN
        self.scopes = [Scope.GMAIL_READ_ONLY_SCOPE_CODE, Scope.GMAIL_MODIFY_SCOPE_CODE]

    def __perform_oauth_login(self) -> Credentials:
        """
        Initiates the OAuth2 flow and returns new credentials.

        :return: New OAuth 2.0 credentials after user login.
        :rtype: Credentials
        """
        flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.scopes)
        return flow.run_local_server(port=0)

    def __load_token(self) -> Credentials | None:
        """
        Loads saved OAuth token from file if it exists.

        :return: The OAuth 2.0 credentials or None if the token doesn't exist.
        :rtype: Credentials or None
        """
        if os.path.exists(self.token_path):
            return Credentials.from_authorized_user_file(self.token_path, self.scopes)
        return None

    def __save_token(self, creds: Credentials) -> None:
        """
        Saves the OAuth 2.0 credentials to a token file.

        :param creds: The OAuth 2.0 credentials to save.
        :return: None
        :rtype: None
        """
        with open(self.token_path, Operation.WRITE) as token_file:
            token_file.write(creds.to_json())


    def get_access_token(self) -> str:
        """
        Returns a valid access token by loading saved credentials,
        refreshing if expired, or performing login if necessary.

        :return: A valid access token string.
        :rtype: str
        """
        creds = self.__load_token()

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                creds = self.__perform_oauth_login()
            self.__save_token(creds)

        return creds.token
