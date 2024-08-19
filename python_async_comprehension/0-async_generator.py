#!/usr/bin/python3
"""the models """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """funciton that make genrator between 0 and 10"""
    for _ in range(0,10):
     await asyncio.sleep(0, 10)
     yield random.uniform(0, 10)
