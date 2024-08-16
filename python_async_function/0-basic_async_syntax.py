 #!/usr/bin/env python3
"""contient méthode asynchrone wait_random"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Simulation opération asynchrone de 0 à max seconds aléatoirement"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
