#!/usr/bin/python3
from db import DB
from user import User
import bcrypt
from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt and return the hashed password as bytes."""
    salt = bcrypt.gensalt()  # Generate a salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
