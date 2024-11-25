import time
from functools import wraps
from utils import log


def stopwatch(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        func(*args, **kwargs)

        run_time = time.time() - start_time
        log.message(f"Test run time is: {run_time} seconds")
    return wrapper

