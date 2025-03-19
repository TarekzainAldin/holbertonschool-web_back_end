#!/usr/bin/env python3
"""
Cache Module

This module provides a Cache class to interact with a Redis database.
It allows storing and retrieving data efficiently using randomly generated keys.
Additionally, it implements method call counting and call history tracking using Redis.
"""

import redis
import uuid
import functools
from typing import Union, Callable, Optional

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.
    
    Args:
        method (Callable): The method to track.
    
    Returns:
        Callable: The wrapped method with counting functionality.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)  # Increment the count in Redis
        return method(self, *args, **kwargs)
    
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.
    
    Args:
        method (Callable): The method to track.
    
    Returns:
        Callable: The wrapped method with history tracking.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))  # Store input arguments
        output = method(self, *args, **kwargs)  # Call original method
        self._redis.rpush(output_key, str(output))  # Store output value
        
        return output
    
    return wrapper

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

    @count_calls
    @call_history
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

    def replay(self, method: Callable):
        """
        Display the history of calls for a particular method.

        Args:
            method (Callable): The method to replay the history for.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Get all inputs and outputs from Redis
        inputs = self._redis.lrange(input_key, 0, -1)  # Get all inputs for the method
        outputs = self._redis.lrange(output_key, 0, -1)  # Get all outputs for the method

        # Display the number of times the method was called
        print(f"{method.__qualname__} was called {len(inputs)} times:")

        # Loop over inputs and outputs to display the history of method calls
        for input_data, output_data in zip(inputs, outputs):
            print(f"{method.__qualname__}(*{eval(input_data.decode('utf-8'))}) -> {output_data.decode('utf-8')}")
