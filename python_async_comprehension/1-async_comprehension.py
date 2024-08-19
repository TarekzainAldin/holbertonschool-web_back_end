#!/usr/bin/env python3
"""contient la méthode asynchrone async_comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Crée liste contenant 10 nbs aléatoires."""
    # Méthode classique
    '''Liste_10_nb_aleatoires = []

    async for yield_value in async_generator():
        Liste_10_nb_aleatoires.append(yield_value)

    return Liste_10_nb_aleatoires'''

    # Autre méthode
    return [yield_value async for yield_value in async_generator()]
