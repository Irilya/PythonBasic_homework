import random


def f(x, y):

    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return round((x / y), 3)


def f2(x, y):

    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return round((y / x), 3)


count_line = 0
try:
    with open('coordinates.txt', 'r') as file:
        with open('result.txt', 'a') as file_2:
            for line in file:
                count_line += 1
                nums_list = line.split()
                try:
                    res1 = f(int(nums_list[0]), int(nums_list[1]))
                    res2 = f2(int(nums_list[0]), int(nums_list[1]))
                    number = random.randint(0, 100)
                    my_list = sorted([str(res1), str(res2), str(number)])
                    my_list = '    '.join(my_list)
                    file_2.write(f'\nСтрока номер {count_line}: {my_list}')
                except ZeroDivisionError:
                    file_2.write(f'\nВ строке {count_line} произошло деление на ноль')
                    print("Делениe на ноль невозможно")
except FileNotFoundError:
    print("Нет такого файла.")

