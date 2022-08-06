import datetime
from typing import Callable, Any
import functools


LOG = dict()


def logging(func: Callable) -> Callable:
    """
    Декоратор логгирования функций. Если во время выполнения функции возникает ошибка,
    то добавляется информация об ошибке и времени ее возникновения.
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        while True:
            try:
                res = func(*args, **kwargs)
                LOG[func.__name__] = func.__doc__
                return res
            except Exception as er:
                time_er = datetime.datetime.today()
                LOG[func.__name__] = [func.__doc__, {time_er.strftime("%Y-%m-%d-%H.%M.%S"): er}]
                break
        return LOG
    return wrapped

#
# @logging
# def test(num: int) -> None:
#     """
#     Функция расчитывает сумму квадратов всех чисел от 0 до num
#     :param num (int):
#     :return: None
#     """
#     summ = 0
#     for item in range(num):
#         res = item ** 2
#         summ += res
#     print(summ)
#
#
# @logging
# def test1() -> None:
#     """
#     Функция деления
#
#     :return: None
#     """
#     res = 15 / 0
#     print(res)
#
#
# @logging
# def rty(name: str) -> None:
#     """
#     Функция приветствия.
#     """
#     print(f'Hello, {name}!')
#
#
# test('gh')
# test1(15)
# rty('Tom')
# for item in LOG:
#     print('{key}:  {value}'.format(key=item, value=LOG[item]))
