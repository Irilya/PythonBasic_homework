import time
from typing import Callable, Any
import functools


def sleep_time(func: Callable) -> Callable:
    """
    Декоратор, реализующий ожидание перед выполнением функции
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        time.sleep(5)
        result = func(*args, **kwargs)
        return result

    return wrapped_func
