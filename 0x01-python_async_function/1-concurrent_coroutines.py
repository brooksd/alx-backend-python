#!/usr/bin/env python3

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asynchronous coroutine that takes in two
    arguments and returns a list
    of all the delays. The number of delays
    is the same as n. The list should be in ascending order
    without using sort().
    """
    wait_list = []

    for i in range(n):
        wait_list.append(await wait_random(max_delay))

    return sorted(wait_list)
