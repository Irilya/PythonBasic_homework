import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator):
    @functools.wraps(decorator)
    def wrapper(*args, **kwargs):
        print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
        return decorator
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func, *args, **kwargs)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
