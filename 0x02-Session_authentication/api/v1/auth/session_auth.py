#!/usr/bin/env python3
"""This module is about SessionAuth"""

from flask import Flask
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
import base64
import binascii
import uuid


from typing import List, TypeVar


class SessionAuth(Auth):
    """SessionAuth class"""

    # class attribute
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create a session id for a user_id
        Return:
            - a Session ID using uuid module and uuid4() or None
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            # add to the dict
            SessionAuth.user_id_by_session_id.update({session_id: user_id})
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """function that return a user_id
        Return:
            - a user ID or None
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        else:
            user_id = SessionAuth.user_id_by_session_id.get(session_id)
            return user_id
