#!/usr/bin/env python3
"""This module is about SessionAuth"""

from flask import Flask
from flask import request
from api.v1.auth.auth import Auth
from models.user import User
import base64
import binascii


from typing import List, TypeVar


class SessionAuth(Auth):
    """SessionAuth class"""
