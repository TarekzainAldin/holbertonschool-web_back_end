#!/usr/bin/env python3

""" Let's execute multiple coroutines at the same time with async """

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure  tarek """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = asyncio.get_event_loop().time()
    return end - start
