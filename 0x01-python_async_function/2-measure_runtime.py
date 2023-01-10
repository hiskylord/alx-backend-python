#!/usr/bin/env python3
"""Contains a method that measure the total execution time of
a function"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of a function
    Args:
        n: the number of coroutines to launch
        max_delay: the maximum amount of time to wait for each coroutine
    Returns: elapsed time in seconds
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
