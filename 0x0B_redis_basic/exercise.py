#!/usr/bin/env python3
"""
    String Redis
"""
from uuid import uuid4
from typing import Union, Callable
from functools import wraps
import uuid
import redis

class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a randomly generated key and return the key."""
        key = str(uuid.uuid4())  # Generate a random UUID as a string
        self._redis.set(key, data)  # Store the data in Redis
        return key
    
    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """
            Store the cache

            Args:
                data: bring the information to store

            Return:
                Key or number uuid
        """
        key = self._redit.get(key)

        if fn:
            return fn(key)

        return key

    def get_str(self, key: str) -> str:
        """ Parametrized get str """
        return self._redit.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Parametrized get int """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0

        return value