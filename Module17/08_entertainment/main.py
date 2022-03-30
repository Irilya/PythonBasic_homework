
import random

number_N = int(input('Количество палок: '))
fence = ['|' for _ in range(number_N)]
cast_numbers = int(input('Количество бросков: '))
count = 1


while count <= cast_numbers:
    print('\nБросок ', count)
    a = random.randint(1, number_N)
    b = random.randint(1, number_N)
    if a > b:
        Right_i, Left_i = a, b
    else:
        Left_i, Right_i = a, b
    print('Сбиты палки с номера ', Left_i, 'по номер ', Right_i)
    for i in range(Left_i - 1, Right_i):
        fence[i] = '.'
    count += 1


print('\nРезультат: ', ''.join(fence))


