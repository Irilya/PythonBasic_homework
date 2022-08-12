from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, мешающий программисту работать. Желает общаться.
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        name = input('Привет! Ты кто? ')
        answer = input(f'A! Привет, {name}! Дела-то как? ')
        print(f'А мне что-то нехорошо, {name}... То лапы ломит, то хвост отваливается...')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@how_are_you
def test(num: int) -> int:
    """
    Функция расчитывает сумму квадратов всех чисел от 0 до num
    :param num (int):
    :return: summ (int)
    """
    summ = 0
    for item in range(num):
        res = item ** 2
        summ += res
    return summ


print(test(15))
