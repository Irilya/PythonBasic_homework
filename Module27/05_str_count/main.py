from typing import Callable, Any
import functools
func_count = {}


def counter(func: Callable) -> Callable:
    """Декоратор, считающий и выводящий количество вызовов декорируемой функции"""
    func_count[func.__name__] = 0

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        res = func(*args, **kwargs)
        func_count[func.__name__] += 1
        print(f'Функция {func.__name__} запущена - {func_count[func.__name__]} раз.')
        return res
    return wrapped

#
# @counter
# def test(num: int) -> None:
#     """
#     Функция расчитывает сумму квадратов всех чисел от 0 до num
#     :param num (int):
#     :return: None
#     """
#     summ = 0
#     for item in range(1, num + 1):
#         res = item ** 2
#         summ += res
#     print(f'Сумма квадратов чисел от 1 до {num} равна: {summ}')
#
#
# @counter
# def test_1():
#     print('Hello!')
#
#
# test(15)
# test(10)
# test(7)
# test_1()
# test_1()
# test_1()


def counter(func: Callable) -> Callable:
    """Декоратор, считающий и выводящий количество вызовов декорируемой функции"""
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        res = func(*args, **kwargs)
        wrapped.count += 1
        print(f'Функция {func.__name__} запущена - {wrapped.count} раз.')
        return res
    wrapped.count = 0
    return wrapped


# @counter
# def test(num: int) -> None:
#     """
#     Функция расчитывает сумму квадратов всех чисел от 0 до num
#     :param num (int):
#     :return: None
#     """
#     summ = 0
#     for item in range(1, num + 1):
#         res = item ** 2
#         summ += res
#     print(f'Сумма квадратов чисел от 1 до {num} равна: {summ}')
#
#
# @counter
# def test_1():
#     print('Hello!')
#
#
# test(15)
# test(10)
# test(7)
# test_1()
# test_1()
# test_1()
