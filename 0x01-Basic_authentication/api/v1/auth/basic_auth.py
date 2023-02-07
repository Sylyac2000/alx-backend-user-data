#!/usr/bin/env python3
"""This module is about BasicAuth"""

from flask import Flask
from flask import request
from api.v1.auth.auth import Auth


from typing import List, TypeVar


class BasicAuth(Auth):
    """BasicAuth class"""
