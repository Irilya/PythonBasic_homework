from collections.abc import Iterator


class SquareNum:
    """
    Класс для создания итерратора квадратов чисел последовательности
    """
    def __init__(self, number: int) -> None:
        self.number = number
        self.count = 0
        self.sq = 0

    def __iter__(self) -> Iterator[int]:
        """
        Метод обнуляет исходные значения и запускает новый цикл итерратора.
        :return:
        """
        self.count = 0
        self.sq = 0
        return self

    def __next__(self):
        """
        Метод позволяет получить следующее значение итерратора
        :return: sq
        :type: int
        """
        self.count += 1
        if self.count <= self.number:
            self.sq = self.count ** 2
            return self.sq
        else:
            raise StopIteration


line = SquareNum(5)
for i in line:
    print(i, end=' ')
print()
line = SquareNum(12)
for i in line:
    print(i, end=' ')
print()


def sqnum(nums: int) -> Iterator[int]:
    """
    Генератор позволяет получить квадраты чисел последовательности
    :param nums:
    :return:
    """
    for i_num in range(1, nums + 1):
        yield i_num ** 2


for i in sqnum(6):
    print(i, end=' ')
print()
for i in sqnum(8):
    print(i, end=' ')
print()


num = int(input('Введите число: '))
for item in (i ** 2 for i in range(1, num + 1)):
    print(item, end=' ')
