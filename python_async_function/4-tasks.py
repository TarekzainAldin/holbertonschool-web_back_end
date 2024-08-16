#!/usr/bin/env python3
""""Contient méthode asynchrone task_wait_n"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """lance n tâches asynchrones 'wait_random' qui s'exécutent en parallèle
    et durent au maximum max_delay secondes"""

    liste_operations = []
    # Boucle pour créer une liste de n opérations asynchrones
    for i in range(n):
        liste_operations.append(task_wait_random(max_delay))

    liste_delais = []
    for operation in asyncio.as_completed(liste_operations):
        delais = await operation
        liste_delais.append(delais)

    return liste_delais
