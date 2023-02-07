#!/usr/bin/env python3
"""This module is about auth"""

from flask import Flask
from flask import request

from typing import List, TypeVar


class Auth():
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth"""
        if path:
            last_char = path[-1:]
            if last_char != '/':
                path += '/'

        if path is None or path not in excluded_paths:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None
