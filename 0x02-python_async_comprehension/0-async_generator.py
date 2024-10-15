#!/usr/bin/env python3
"""
An Async generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A function that has a coroutine looping 10 times.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
