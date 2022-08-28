from typing import Union


class Figure:
    perimeter = 0
    square = 0
    name = 'Figure'
    """
    Базовый класс Фигура

    Args and attrs:
        attribut_1 (Union[int, float]): длина стороны / основание треугольника
        attribut_2 (Union[int, float]): длина стороны / высота треугольника
    """

    def __init__(self, base: Union[int, float] = 0, height: Union[int, float] = 0) -> None:
        self.base = base
        self.height = height

    @property
    def base(self) -> Union[int, float]:
        """Геттер. Возвращает attribute_1"""
        return self._base

    @property
    def height(self) -> Union[int, float]:
        """Геттер. Возвращает attribute_2"""
        return self._height

    @base.setter
    def base(self, base) -> None:
        """Сеттер. Устанавливает attribute_1"""
        self._base = base

    @height.setter
    def height(self, height) -> None:
        """Сеттер. Устанавливает attribute_1"""
        self._height = height

    def get_perimeter(self):
        pass

    def get_square(self):
        pass


class Sguare(Figure):
    """
    Класс Квадрат. Родительский класс - базовый класс Фигура
    """
    name = 'Sguare'

    def get_perimeter(self) -> Union[int, float]:
        """
        Метод для получения периметра фигуры.
        :return (Union[int, float]):
        """
        perimeter = 4 * self.base
        return perimeter

    def get_square(self) -> Union[int, float]:
        """
        Метод для получения площади фигуры.
        :return (Union[int, float]):
        """
        square = self.base ** 2
        return square


class Triangle(Figure):
    """
    Класс треугольник. Родительский класс - базовый класс Фигура
    """
    name = 'Треугольник'

    def get_perimeter(self) -> Union[int, float]:
        """
        Метод для получения периметра фигуры.
        :return (Union[int, float]):
        """
        perimeter = self.base + 2 * (((self.base / 2) ** 2) + self.height ** 2) ** 0.5
        return perimeter

    def get_square(self) -> Union[int, float]:
        """
        Метод для получения площади фигуры.
        :return (Union[int, float]):
        """
        square = 1 / 2 * self.base * self.height
        return square


class Cube(Sguare):
    """
    Класс Cube. Родительский класс - класс Sguare
    """
    name = 'Cube'

    def __init__(self, base):
        super().__init__(base, height=0)
        self.edge_square = Sguare(self.base)

    def get_perimeter(self) -> Union[int, float]:
        """
        Метод для получения периметра фигуры.
        :return (Union[int, float]):
        """
        perimeter = 12 * self.base
        return perimeter

    def get_square(self) -> Union[int, float]:
        """
        Метод для получения площади фигуры.
        :return (Union[int, float]):
        """
        square = self.edge_square.get_square() * 6
        return square


class Pyramid(Sguare, Triangle):
    """
    Класс Pyramid. Родительские классы - класс Sguare и класс Triangle
    """
    name = 'Pyramid'

    def __init__(self, base, height):
        super().__init__(base, height)
        self.edge_square = Sguare(self.base)
        self.edge_triangle = Triangle(self.base, self.height)

    def get_perimeter(self) -> Union[int, float]:
        """
        Метод для получения периметра фигуры.
        :return (Union[int, float]):
        """
        perimeter = 2 * self.base + 2 * self.edge_triangle.get_perimeter()
        return perimeter

    def get_square(self) -> Union[int, float]:
        """
        Метод для получения площади фигуры.
        :return (Union[int, float]):
        """
        square = self.edge_square.get_square() + (4 * self.edge_triangle.get_square())
        return square


figurs = [Sguare(base=6),
          Triangle(base=5, height=8),
          Cube(base=3),
          Pyramid(base=5, height=6)]
for item in figurs:
    print(f'Периметр {item.name} с параметрами ({item.base},{item.height}) '
          f'составляет {item.get_perimeter()}')
    print(f'Площадь {item.name} с параметрами ({item.base},{item.height}) '
          f'составляет {item.get_square()}')


# Слишком много вариантов решения, уже устала улучшать.)) Это уже третий вариант. Пробовала делать
# как в обсуждении, держать, допустим, шесть поверхностей списком в кубе и получать площадь через цикл,
# но так и не поняла чем это лучше. Оставила свой вариант, пожалуйста, на сравнении объясните мне какой
# питоничнее. Пробовала базовый класс делать абстрактным, тоже работает, но там инит надо было везде
# прописывать. Так и не придумала как сюда пришить миксин. Делать что-то искусственно не хотелось.
# Одним словом, наигралась.))) Пришла к выводу, что выбор варианта зависит от конкретных сиюминутных задач,
# а так же от необходимости трансформации программы в дальнейшем. Нужно больше практики.
# Спасибо, что дочитали.
