#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions:
    
    coroutine that takes no
    arguments. The coroutine will execute async_comprehension
    four times in parallel using asyncio.gather.
    Returns:
        The total runtime.
    """
    
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
