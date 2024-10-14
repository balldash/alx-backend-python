#!usr/bin/python3
"""
The basic syntax of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay duration.
    """
    randomDelay = random.uniform(0, max_delay)
    await asyncio.sleep(randomDelay)
    return randomDelay
