#!/usr/bin/env python3
"""contient la méthode measure_runtime"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute 4 fois async_comprehension de maniere asynchrone
    et mesure le temps d'exécution total. """
    tic = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    tac = time.time()
    return (tac - tic)
    # On obtient un temps d'exécution d'environ 10 secondes car les 4 appels
    # sont exécutés en parallèle et chacun prend environ 10 x 1 secondes.