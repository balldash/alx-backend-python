#!/usr/bin/env python3
"""
Run time for four parallel comprehensions.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A function that measures the total runtime and returns it.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.perf_counter() - start
