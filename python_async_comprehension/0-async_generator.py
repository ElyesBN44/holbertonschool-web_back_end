#!/usr/bin/env python3
"""This module defines an asynchronous generator that yields random numbers
between 0 and 10."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield a random float between 0 and 10, 10 times.
    This asynchronous generator yields random floating point numbers
    between 0 and 10, waiting 1 second between each yield.
    Yields:
    float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
