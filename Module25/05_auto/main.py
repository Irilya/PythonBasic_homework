import math


class Automobil:
    """
    Базовый класс, описывающий автомобиль и его положение в пространстве.

    Args:
        coordinate_x (float) - передается координата по оси Х положения автомобиля
        coordinate_y (float) - передается координата по оси Y положения автомобиля
        angle (float) - передается угол, описывающий направление движения (в радианах).
        distance (int) - передается пройденное расстояние
    """

    def __init__(self, coordinate_x, coordinate_y, angle, distance=0):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.angle = angle
        self.distance = distance

    def __str__(self):
        """
        Метод для получения строкового вида объекта класса Automobil.

        :rtype: str
        """

        return f'Автомобиль находится в точке с координатами {self.coordinate_x}, {self.coordinate_y}'

    def moving(self, angle, distance):
        """
        Метод для расчета новых координат положения автомобиля после перемещения
        :param angle: (float) - угол, описывающий направление движения (в радианах).
        :param distance: (int) - пройденное расстояние
        :return: self.coordinate_x: float, self.coordinate_y: float
        """

        print(f'Автомобиль начал движение из точки '
              f'с координатами {self.coordinate_x}, {self.coordinate_y}')

        if 0 < angle < math.pi / 2:
            self.coordinate_x += distance * math.cos(angle)
            self.coordinate_y += distance * math.sin(angle)
        elif math.pi / 2 < angle < math.pi:
            self.coordinate_x -= distance * math.cos(angle)
            self.coordinate_y += distance * math.sin(angle)
        elif math.pi < angle < math.pi * 1.5:
            self.coordinate_x += distance * math.cos(angle)
            self.coordinate_y -= distance * math.sin(angle)
        else:
            self.coordinate_x -= distance * math.cos(angle)
            self.coordinate_y -= distance * math.sin(angle)

        print(f'Автомобиль проехал {distance} км и прибыл в точку '
              f'с координатами {self.coordinate_x}, {self.coordinate_y}')
        return self.coordinate_x, self.coordinate_y


class Bus(Automobil):
    """
    Класс Bus, описывающий автобус и его положение в пространстве. Родительский класс - Automobil.

    Args:
        coordinate_x (float) - передается координата по оси Х положения автомобиля
        coordinate_y (float) - передается координата по оси Y положения автомобиля
        angle (float) - передается угол, описывающий направление движения (в радианах).
        distance (int) - передается пройденное расстояние
        pas_count (int) - количество пассажиров в салоне автобуса
        money (float) - сумма денег в кассе
    """

    def __init__(self, coordinate_x, coordinate_y, angle, distance, pas_count=0, money=0):
        super().__init__(coordinate_x, coordinate_y, angle, distance)
        self.pas_count = pas_count
        self.money = money

    def __str__(self):
        """
        Метод переназначен для получения строкового вида объекта класса Bus.

        :rtype: str
        """

        return f'Автобус находится в точке с координатами {self.coordinate_x}, {self.coordinate_y}, ' \
               f'количество пассажиров в салоне: {self.pas_count}, ' \
               f'сумма, вырученая от продажи билетов: {self.money}'

    def enter(self, count):
        """
        Метод для подсчета общего количества пассажиров в салоне после посадки
        :param count: (int) - количество вошедших пассажиров
        :return: pas_count (int)
        """

        self.pas_count += count
        print(f'Вошло {count} человек')
        return self.pas_count

    def go_out(self, count):
        """
        Метод для подсчета общего количества пассажиров в салоне после высадки
        :param count: (int) - количество вышедших пассажиров
        :return: pas_count (int)
        """

        self.pas_count -= count
        print(f'Вышло {count} человек')
        return self.pas_count

    def moving(self, angle, distance, cost_km=0.1):
        """
        Метод переназначен для расчета новых координат автобуса после перемещения автобуса, а также
        для расчета полученных денег от продажи белетов для (pas_count) пассажиров в салоне
        при перемещении на заданное растояние (distance).
        :param angle: (float) - угол, описывающий направление движения (в радианах).
        :param distance: (int) - пройденное расстояние
        :param cost_km: (float) - стоимость одного км для одного пассажира
        :return: self.coordinate_x: float, self.coordinate_y: float, self.money: float
        """

        print(f'Автобус начал движение из точки '
              f'с координатами {self.coordinate_x}, {self.coordinate_y}')

        if 0 < angle < math.pi / 2:
            self.coordinate_x += distance * math.cos(angle)
            self.coordinate_y += distance * math.sin(angle)
        elif math.pi / 2 < angle < math.pi:
            self.coordinate_x -= distance * math.cos(angle)
            self.coordinate_y += distance * math.sin(angle)
        elif math.pi < angle < math.pi * 1.5:
            self.coordinate_x += distance * math.cos(angle)
            self.coordinate_y -= distance * math.sin(angle)
        else:
            self.coordinate_x -= distance * math.cos(angle)
            self.coordinate_y -= distance * math.sin(angle)
        self.coordinate_x = round(self.coordinate_x, 4)
        self.coordinate_y = round(self.coordinate_y, 4)

        self.money += cost_km * distance * self.pas_count
        self.money = round(self.money, 2)
        return self.coordinate_x, self.coordinate_y, self.money


avtobus = Bus(2, 2, 0, 0)
print(avtobus)
avtobus.enter(8)
print(avtobus)
avtobus.moving(1.2, 3)
avtobus.go_out(3)
print(avtobus)

