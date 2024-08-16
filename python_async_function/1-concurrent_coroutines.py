#!/usr/bin/env python3
""""contient méthode asynchrone wait_n"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """lance n tâches asynchrones 'wait_random' qui s'exécutent en parallèle
    et dure au maximum max_delay secondes"""

    liste_operations = []
    # Boucle pour créer une liste de n operations asynchrones
    for i in range(n):
        liste_operations.append(wait_random(max_delay))

    # lance et attend que toutes les opérations de la liste soient terminées
    '''liste_delais = await asyncio.gather(*liste_operations)

    return sorted(liste_delais)'''

    # autre solution
    liste_delais = []
    for operation in asyncio.as_completed(liste_operations):
        delais = await operation
        liste_delais.append(delais)

    return liste_delais
