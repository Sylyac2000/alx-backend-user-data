#!/usr/bin/env python3
"""This module is about BasicAuth"""

from flask import Flask
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
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
        """check if string is base64"""
        try:
            base64.b64decode(string, validate=True)
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
                           base64_authorization_header,
                           validate=True).decode('utf-8')
            return str_decoded

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> str:
        """extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        sub_str = ':'
        if sub_str not in decoded_base64_authorization_header:
            return None, None
        else:
            str_decoded = decoded_base64_authorization_header.split(':')
            return str_decoded[0], str_decoded[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """get user object from credentials"""
        if user_email is None:
            return None
        if user_pwd is None:
            return None
        if not isinstance(user_email, str) and not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]
        return None
