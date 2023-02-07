#!/usr/bin/env python3
"""This module is about BasicAuth"""

from flask import Flask
from flask import request
from api.v1.auth.auth import Auth


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
