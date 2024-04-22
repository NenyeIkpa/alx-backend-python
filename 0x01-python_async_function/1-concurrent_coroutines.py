#!/usr/bin/env python3

""" Multiple coroutines with async """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    # Create a priority queue to store tasks based on their completion time
    queue = asyncio.PriorityQueue()

    # Function to execute wait_random and store the result in the queue
    async def run_task():
        delay = await wait_random(max_delay)
        await queue.put((delay, delay))

    # Create and schedule all the tasks
    tasks = [run_task() for _ in range(n)]
    await asyncio.gather(*tasks)

    # Retrieve results from the queue in ascending order
    results = []
    while not queue.empty():
        _, delay = await queue.get()
        results.append(delay)

    return results
