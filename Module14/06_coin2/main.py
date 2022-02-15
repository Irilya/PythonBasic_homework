import math


def coin_coordinate():


    coordinate_x = float(input('Введите координату монетки - x: '))
    coordinate_y = float(input('Введите координату монетки - y: '))
    circle_radius = float(input('Введите радиус круга: '))
    circle_area = circle_radius ** 2 * math.pi
    if coordinate_x >= coordinate_y:
        coin_circle_area = coordinate_x ** 2 * math.pi
    else:
        coin_circle_area = coordinate_y ** 2 * math.pi
    if coin_circle_area <= circle_area:
        print('Монетка где-то рядом.')
    else:
        print('Монетки в круге нет.')


coin_coordinate()










