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


def _generate_uuid() -> str:
    """generate uuid
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """validate login
            Return:
                bool
        """
        if not email or not password:
            return False
        try:
            user = self._db.find_user_by(email=email)
            is_correct_pwd = is_valid(user.hashed_password, password)
            return is_correct_pwd
        except (NoResultFound, InvalidRequestError):
            return False

    def valid_user(self, email: str) -> User:
        """valid_user email
            Return:
                user object
        """
        if not email:
            return None
        try:
            user = self._db.find_user_by(email=email)
            return user
        except (NoResultFound, InvalidRequestError):
            return None

    def create_session(self, email: str) -> str:
        """create_session
            Return:
                session id
        """
        user = self.valid_user(email)
        if user is not None:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """get user by session id
            Return:
                a user object
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except (NoResultFound, InvalidRequestError):
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroy session by user_id
            Return:
                None
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """reset password token
            Return:
                String
        """
        user = self.valid_user(email)
        if user is None:
            raise ValueError(f"User {email} not exists")
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token
