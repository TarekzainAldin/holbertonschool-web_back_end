#!/usr/bin/python3

from user import user
from db import DB


from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NotResulteFound



def _hash_password(password: str) -> str:
  """ Takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
  return hashpw(password.encode('utf-8'), gensalt())
