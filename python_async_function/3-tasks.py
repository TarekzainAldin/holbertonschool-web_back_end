#!/usr/bin/env python3
"""contient la fonction task_wait_random"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """créé une tâche asynchrone qui attend un temps aléatoire"""
    return asyncio.create_task(wait_random(max_delay))
