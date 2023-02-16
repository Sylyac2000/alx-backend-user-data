#!/usr/bin/env python3
"""module to encrypt
"""
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """return hashed password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if password is valid, correct"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register a user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            str_pwd_hashed = _hash_password(password)
            user = self._db.add_user(email=email,
                                     hashed_password=str_pwd_hashed)
            return user

    def valid_login(self, email, password) -> bool:
        """validate login
            Return:
                bool
        """
        try:
            user = self._db.find_user_by(email=email)
            is_correct_pwd = is_valid(user.hashed_password, password)
            return is_correct_pwd
        except NoResultFound:
            return False

    def _generate_uuid() -> str:
        """generate uuid
        """
        return uuid.uuid4()
