#!/usr/bin/env python3

""" Multiple coroutines with async """

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """ spawns multiple corountines """
    values = []
    for i in range(n):
       values.append(wait_random(max_delay))
    result = await asyncio.gather(*values)
    return result
