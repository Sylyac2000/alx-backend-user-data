#!/usr/bin/env python3
"""This module is about BasicAuth"""

from flask import Flask
from flask import request
from api.v1.auth.auth import Auth
import base64
import binascii


from typing import List, TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base 64 """
        if authorization_header is None:
            return None
        # print(type(authorization_header))
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            str_header = authorization_header.split('Basic ')
            return str_header[1]

    def is_base64(self, string: str) -> bool:
        try:
            base64.b64decode(string)
            return True
        except binascii.Error:
            return False

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        if not self.is_base64(base64_authorization_header):
            return None
        else:
            str_decoded = base64.b64decode(
                           base64_authorization_header).decode('utf-8')
            return str_decoded
