#!/usr/bin/env python3
"""
Cache Module

This module provides a Cache class to interact with a Redis database.
It allows storing and retrieving data efficiently using randomly generated keys.
"""

import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    """
    Cache class to handle storing and retrieving data in Redis.

    Attributes:
        _redis (redis.Redis): Redis client instance.
    """
    
    def __init__(self):
        """
        Initialize the Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.
        
        Returns:
            str: The generated key used to store the data.
        """
        key = str(uuid.uuid4())  # Generate a random UUID as a string
        self._redis.set(key, data)  # Store the data in Redis
        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and apply an optional conversion function.

        Args:
            key (str): The Redis key to retrieve data for.
            fn (Optional[Callable]): A function to convert the retrieved data.
        
        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, converted if a function is provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data
    
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The Redis key to retrieve data for.
        
        Returns:
            Optional[str]: The retrieved string data.
        """
        return self.get(key, lambda d: d.decode('utf-8'))
    
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The Redis key to retrieve data for.
        
        Returns:
            Optional[int]: The retrieved integer data.
        """
        return self.get(key, lambda d: int(d))
