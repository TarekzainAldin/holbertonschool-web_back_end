#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from bcrypt import gensalt, hashpw, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password string using bcrypt and return the salted hash"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """Generate a string representation of a new UUID."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if the email does not exist,
            else raise ValueError.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Checks if user pswd is valid, locating by email """
        try:
            found_user = self._db.find_user_by(email=email)
            return checkpw(
                password.encode('utf-8'),
                found_user.hashed_password
                )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Creates session ID using UUID, finds user by email """
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(found_user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """ Finds user by session_id """
        if session_id is None:
            return None
        try:
            found_user = self._db.find_user_by(session_id=session_id)
            return found_user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: str) -> None:
        """ Updates user's session_id to None """
        if user_id is None:
            return None
        try:
            found_user = self._db.find_user_by(id=user_id)
            self._db.update_user(found_user.id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Finds user by email, updates user's
          reset_token with UUID, and returns the token.
        Args:
            email (str): The email of the user requesting a password reset.
        Returns:
            str: The newly generated reset token.
        Raises:
            ValueError: If no user with the given email is found.
        """
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User not found")

        reset_token = str(uuid.uuid4())  # Generate a new UUID string
        self._db.update_user(found_user.id, reset_token=reset_token)
        return reset_token
