import redis
import uuid
import functools
from typing import Union, Callable, Optional

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.
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
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))  # Store input arguments
        output = method(self, *args, **kwargs)  # Call the original method
        self._redis.rpush(output_key, str(output))  # Store output value
        
        return output
    return wrapper

class Cache:
    """
    Cache class to handle storing and retrieving data in Redis.
    """
    
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())  # Generate a random UUID as a string
        self._redis.set(key, data)  # Store the data in Redis
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data
    
    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, lambda d: d.decode('utf-8'))
    
    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, lambda d: int(d))

    def replay(self, method: Callable):
        """
        Replay the history of calls for a given method.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for input_data, output_data in zip(inputs, outputs):
            print(f"{method.__qualname__}(*{eval(input_data.decode('utf-8'))}) -> {output_data.decode('utf-8')}")

# Use the Cache class and replay function
if __name__ == "__main__":
    cache = Cache()

    # Store some data
    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    # Replay the history
    cache.replay(cache.store)
