#!/usr/bin/env python3
"""This module is about encrypting password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ return hashed password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
