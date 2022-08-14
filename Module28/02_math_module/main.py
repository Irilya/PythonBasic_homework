import math
from abc import ABC
from typing import Union


class MyMath(ABC):
    """
    Абстрактный базовый класс как модуль для функций, которые можно использовать без создания
    экземпляра класса.
    """
    @classmethod
    def circle_len(cls, radius: Union[int, float]) -> Union[int, float]:
        """Функция расчета длины окружности"""
        cir_len = 2 * math.pi * radius
        return cir_len

    @classmethod
    def circle_sq(cls, radius: Union[int, float]) -> Union[int, float]:
        """Функция расчета площади окружности"""
        cir_sq = math.pi * radius ** 2
        return cir_sq

    @classmethod
    def sphere_square(cls, radius: Union[int, float]) -> Union[int, float]:
        """Функция расчета площади шара"""
        sq_sph = 4 * math.pi * radius ** 2
        return sq_sph

    @classmethod
    def sphere_volume(cls, radius: Union[int, float]) -> Union[int, float]:
        """Функция расчета объема шара"""
        vol_sph = 4 / 3 * math.pi * radius ** 3
        return vol_sph

    @classmethod
    def square_perimeter(cls, length: Union[int, float]) -> Union[int, float]:
        """Функция расчета периметра квадрата"""
        sq_per = 4 * length
        return sq_per

    @classmethod
    def square_sq(cls, length: Union[int, float]) -> Union[int, float]:
        """Функция расчета площади квадрата"""
        sq_sq = length ** 2
        return sq_sq

    @classmethod
    def cube_sq(cls, length: Union[int, float]) -> Union[int, float]:
        """Функция расчета площади куба"""
        c_sq = 6 * length ** 2
        return c_sq

    @classmethod
    def cube_volume(cls, length: Union[int, float]) -> Union[int, float]:
        """Функция расчета объема куба"""
        cube_v = length ** 3
        return cube_v


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.sphere_volume(8)
print(res_1)
print(res_2)
print(res_3)
#
# Вот все-таки думаю - не лучше ли тут использовать staticmethod, учитывая,
# что кроме вызова функций из модуля, действий больше не предвидится. Все-таки
# экономия памяти?...
