import redis
import uuid
from typing import Union

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