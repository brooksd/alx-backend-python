#!/usr/bin/env python3

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that takes a parameter,
    waits for a random delay and returns the value
    of the delay.
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
