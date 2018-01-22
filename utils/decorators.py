from functools import wraps
import time


def time_this(function_to_time):
    """
    decorator used to time functions
    """
    @wraps(function_to_time)
    def timer(*args, **kwargs):
        start = time.time()
        result = function_to_time(*args, **kwargs)
        end = time.time()
        exec_time = end-start
        return result, exec_time

    return timer

