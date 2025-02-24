#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True) 
    reset_token = Column(String(250), nullable=True)  

    def __repr__(self):
        return f"<User(email='{self.email}', hashed_password='{self.hashed_password}', session_id='{self.session_id}')>"

