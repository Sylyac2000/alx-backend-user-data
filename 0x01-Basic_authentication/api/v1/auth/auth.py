#!/usr/bin/env python3
"""This module is about auth"""

from flask import Flask
from flask import request

from typing import List, TypeVar


class Auth():
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth"""
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for apath in excluded_paths:
                if apath.startswith(path):
                    return False
                if path.startswith(apath):
                    return False
                if apath[-1] == "*":
                    if path.startswith(apath[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None
