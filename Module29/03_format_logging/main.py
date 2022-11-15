import functools
import time
from typing import Callable


def log_methods(timenow):

    @functools.wraps(timenow)
    def decorate(cls):
        def timer(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                print(f'Запускается "{cls.__name__}.{func.__name__}". Дата и время запуска: {timenow}')
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f'Завершение функции "{cls.__name__}.{func.__name__}". Время работы: {round(end - start, 4)}')
                return result
            return wrapped
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = timer(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@log_methods('Apr 23 2021 - 21:50:37')
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods('Apr 23 2021 - 21:50:37')
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
