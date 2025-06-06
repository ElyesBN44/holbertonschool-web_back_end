#!/usr/bin/env python3
"""This module measures the runtime of running async_comprehension
four times in parallel."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of running async.
    This coroutine executes async_comprehension four times concurrently
    using asyncio.gather and measures the total runtime.
    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
