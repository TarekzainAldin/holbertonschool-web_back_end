 #!/usr/bin/env python3
"""c
ontient méthode
 asynchrone 
 wait_random"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Simulation opération asynchrone de 0"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
