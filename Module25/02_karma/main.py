import random


class KillError(Exception):
    def __str__(self):
        return 'Убийство смертный грех!!!'


class DrunkError(Exception):
    def __str__(self):
        return 'Вы пропили свое просветление!'


class CarCrashError(Exception):
    def __str__(self):
        return 'Вы ушли на новый круг перерождения! Соблюдайте правила ПДД!'


class GluttonyError(Exception):
    def __str__(self):
        return 'Ваш лишний вес не позволяет Вам вознестись!'


class DepressionError(Exception):
    def __str__(self):
        return 'Вам не нравится Ваша жизнь? Мы предоставим Вам другую, ' \
               'чтобы Вы поняли как хороша была эта!'


def one_day():

    enlightenment = 500
    total_carma = 0
    day_count = 0

    while total_carma < enlightenment:
        day_count += 1
        print(f'День - {day_count}')
        choice = random.randint(0, 50)
        if choice == 0:
            try:
                raise KillError
            except KillError as exp:
                print(str(exp))
                with open('karma.log', 'a', encoding='utf-8') as karma:
                    karma.write(f'\nДень - {day_count}\t{exp}')
        elif choice == 10:
            try:
                raise DrunkError
            except DrunkError as exp:
                print(exp)
                with open('karma.log', 'a', encoding='utf-8') as karma:
                    karma.write(f'\nДень - {day_count}\t{exp}')
        elif choice == 20:
            try:
                raise CarCrashError
            except CarCrashError as exp:
                print(exp)
                with open('karma.log', 'a', encoding='utf-8') as karma:
                    karma.write(f'\nДень - {day_count}\t{exp}')
        elif choice == 30:
            try:
                raise GluttonyError
            except GluttonyError as exp:
                print(exp)
                with open('karma.log', 'a', encoding='utf-8') as karma:
                    karma.write(f'\nДень - {day_count}\t{exp}')
        elif choice == 40:
            try:
                raise DepressionError
            except DepressionError as exp:
                print(exp)
                with open('karma.log', 'a', encoding='utf-8') as karma:
                    karma.write(f'\nДень - {day_count}\t{exp}')
        else:
            carma = random.randint(1, 7)
            print(f'Ваша карма улучшилась на {carma} пунктов.')
            total_carma += carma

    print(f'Поздравляю! На {day_count} день Вы достигли просветления, набрали кармы - {total_carma}')


one_day()

