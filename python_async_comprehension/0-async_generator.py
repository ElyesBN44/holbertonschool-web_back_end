#!/usr/bin/env python3
"""Module containing an asynchronous generator coroutine."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random float between 0 and 10 asynchronously
    10 times, each after a 1 second wait.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
