"""
This module contains all decorators for test framework.
"""
import time

from utils import log


def stopwatch(func):
    """
    This decorator can be used to measure the time.
    :param func: function to be decorated
    :return: decorated function
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()

        func(*args, **kwargs)

        run_time = time.time() - start_time
        log.message(f"Test runtime is: {run_time} seconds")
    return wrapper
