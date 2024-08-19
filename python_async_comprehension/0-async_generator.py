#!/usr/bin/env python3
""" Contient la méthode asynchrone async_generator"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Contient une coroutine qui génère 10x des nombres aléatoires de [0, 10[
        toutes les secondes"""

    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
