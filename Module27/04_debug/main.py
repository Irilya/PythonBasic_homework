from typing import Callable, Any
import functools


def debug(func: Callable) -> Callable:
    """
    Декоратор, выводящий имя функции, ее аргументы, а затем — какое значение она возвращает.
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        arg_str = [x.__repr__() for x in args]
        kwarg_str = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(arg_str + kwarg_str)
        print(f'Вызывается {func.__name__}({signature})')
        print(f'{func.__name__!r} вернула значение: {func(*args, **kwargs)!r}')
        res = func(*args, **kwargs)
        print(res)
        return res
    return wrapped


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
