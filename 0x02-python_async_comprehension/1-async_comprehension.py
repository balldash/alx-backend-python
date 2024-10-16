#!/usr/bin/env python3
"""
An Async comprehension module.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function will collect 10 random numbers and return them.
    """
    values = [i async for i in async_generator()]
    return values
