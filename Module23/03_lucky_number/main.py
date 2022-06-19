import random


errors = [
    'Вас постигла неудача!',
    'Опять не пошло!',
    'Что-то пошло не так!',
    'Сегодня не Ваш день!'
    ]
num_summ = 0
while num_summ < 777:
    try:
        with open("out_file.txt", 'a') as answer:
            numero = int(input('Введите число: '))
            num_summ += numero
            if random.randint(0, 13) == 13:
                raise Exception(random.choice(errors))
            else:
                answer.write(f'\nВведено число: {numero}')
    except Exception:
        print(Exception)
        raise
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')
