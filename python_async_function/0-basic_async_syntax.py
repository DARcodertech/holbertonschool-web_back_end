#!/usr/bin/env python3
"""
return a courontine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """return a courontine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
