"""
Created By: Prem Kumar R on 24-05-2025 at 12 PM
"""

from base64 import urlsafe_b64decode
from datetime import datetime

import requests

from auth.oauth2 import OAuth2Auth
from constant import Headers, RequestParam, GmailResponse, Encoding, HTTPMethod, GmailAPI, EmailColumn


class GmailService:
    """
    A class to interact with the Gmail API using raw HTTP requests.
    Fetches and processes messages from the user's inbox.
    """

    def __init__(self, max_results: int = 10):
        self.access_token = OAuth2Auth().get_access_token()
        self.base_url = GmailAPI.LIST_MESSAGES
        self.headers = {Headers.AUTHORIZATION: f'Bearer {self.access_token}'}
        self.max_results = max_results

    def __get_message_ids(self) -> list:
        """
        Fetches message IDs from the user's Gmail inbox.

        :return: A list of message ID strings from the inbox.
        :rtype: List
        """
        response = requests.get(
            f'{self.base_url}',
            headers=self.headers,
            params={
                RequestParam.LABEL_IDS: RequestParam.INBOX,
                RequestParam.MAX_RESULTS: self.max_results
            }
        ).json()
        message_list = response.get(GmailResponse.MESSAGES, [])
        return [message[GmailResponse.ID] for message in message_list]

    @staticmethod
    def __decode_base64_body(data: str) -> str:
        """
        Decode a base64 encoded message body safely.

        :param str data: Message body data
        :return: Decoded message
        :rtype: str
        """
        return urlsafe_b64decode(data).decode(Encoding.UTF, errors='ignore')

    def __extract_body(self, payload: dict) -> str:
        """
        Extracts plain text email body from the payload.

        :param payload: Payload of the gmail message
        :return: Decoded message data
        :rtype: str
        """
        if parts := payload.get(GmailResponse.PARTS, []):
            for part in parts:
                if part.get(GmailResponse.MIME_TYPE):
                    return self.__decode_base64_body(part.get(GmailResponse.BODY, {}).get(GmailResponse.DATA, ''))
        return self.__decode_base64_body(payload.get(GmailResponse.BODY, {}).get(GmailResponse.DATA, ''))

    @staticmethod
    def __extract_header_value(headers: list, key: str) -> str:
        """
        Extracts a specific header value by key name.
        """
        return next((h[GmailResponse.VALUE] for h in headers if h.get(GmailResponse.NAME) == key), f'(No {key})')

    @staticmethod
    def __convert_to_readable_timestamp(date: str) -> datetime:
        """
        Convert the internalDate field creation timestamp epoch ms to readable timestamp.

        :param str date: Timestamp
        :return:
        """
        return datetime.fromtimestamp(int(date) / 1000)

    def __construct_message_column(self, message: dict) -> dict:
        """
        Construct the gmail message to the sql column format

        :param dict message: Gmail message
        :return: Sql column format
        :rtype: dict
        """
        payload = message[GmailResponse.PAYLOAD]
        headers = payload[GmailResponse.HEADERS]
        return {
            EmailColumn.ID: message[GmailResponse.ID],
            EmailColumn.SUBJECT: self.__extract_header_value(headers, GmailResponse.SUBJECT),
            EmailColumn.FROM: self.__extract_header_value(headers, GmailResponse.FROM),
            EmailColumn.TO: self.__extract_header_value(headers, GmailResponse.TO),
            EmailColumn.BODY: self.__extract_body(payload),
            EmailColumn.RECEIVED_AT: self.__convert_to_readable_timestamp(message[GmailResponse.INTERNAL_DATE]),
            EmailColumn.LABELS: ",".join(message[GmailResponse.LABEL_IDS])
        }

    def get_messages(self) -> list:
        """
        Fetches full message details from Gmail and returns them.

        :return: Constructed message details
        :rtype: list
        """
        messages_info = []
        message_ids = self.__get_message_ids()

        for message_id in message_ids:
            message = requests.get(
                f'{self.base_url}/{message_id}',
                headers=self.headers
            ).json()
            message_info = self.__construct_message_column(message)
            messages_info.append(message_info)

        return messages_info

    def update_message(self, message_id: str, payload: dict) -> dict:
        """
        Updates message by adding or removing labels.

        :param str message_id: Message id
        :param dict payload: Values to be updated
        :return: Message
        :rtype: dict
        """
        url = GmailAPI.MODIFY_MESSAGE.format(message_id=message_id)
        return requests.request(method=HTTPMethod.POST, url=url, headers=self.headers, json=payload).json()
