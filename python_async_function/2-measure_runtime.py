#!/usr/bin/env python3
"""contient la fonction measure_time"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """retourne le temps d'execution de la fonction wait_n
    qui est le temps d'execution de la coroutine la plus longue"""
    delais = asyncio.run(wait_n(n, max_delay))
    return (max(delais))
