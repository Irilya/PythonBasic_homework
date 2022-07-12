import random


class Person:

    def __init__(self, name, house, satiety=50):

        self.name = name
        self.satiety = satiety
        self.house = house

    def info_person(self):

        print(f'{self.name}. Сытость: {self.satiety }')

    def eat_food(self):

        print('Пора кушать! Умн-умн, вкусно!')
        self.satiety += 10
        self.house.refrigerator_food -= 10

    def work(self):

        print('Надо бы поработать немного.Кто не работает, тот не ест.')
        self.satiety -= 15
        self.house.money_table += 15

    def play(self):

        print('Ура! Есть время порубать в Циву!')
        self.satiety -= 10

    def shoping(self):

        print('Опять есть нечего! Надо сходить в магазин.')
        self.house.refrigerator_food += 20
        self.house.money_table -= 15


class House:

    def __init__(self, refrigerator_food=50, money_table=0):

        self.refrigerator_food = refrigerator_food
        self.money_table = money_table

    def info_house(self):

        print(f'Всего в доме: еды: {self.refrigerator_food}, денег: {self.money_table}')


def what_we_doing_today(house, people, count=1):

    house.info_house()

    while count <= 365:
        cube_res = random.randint(1, 6)
        print(f'День {count}')
        house.info_house()
        print(f'На кубике сегодня: {cube_res}')
        for i_men in people:
            if i_men.satiety > 0:
                i_men.info_person()
                if i_men.satiety < 20 and house.refrigerator_food > 0:
                    i_men.eat_food()
                elif house.money_table < 50:
                    i_men.work()
                elif house.refrigerator_food < 10 and house.money_table >= 20:
                    i_men.shoping()
                elif cube_res == 1:
                    i_men.work()
                elif cube_res == 2:
                    i_men.eat_food()
                else:
                    i_men.play()

            else:
                print(f'{i_men.name}, вы умерли от голода! Земля пухом!')
                print(f'Мы похоронили {i_men.name}а')
                choice = input('Продолжить? y/n ')
                if choice == 'y':
                    people.remove(i_men)
                    if len(people) > 0:
                        what_we_doing_today(house, people, count)
                    else:
                        break
                else:
                    break
        count += 1


count_men = int(input('Сколько людей живет в доме? '))
my_house = House()
beboere = []
for i_count in range(1, count_men + 1):
    beboere_name = input(f'Как зовут {i_count} жителя дома? ')
    i_count = Person(beboere_name, my_house)
    beboere.append(i_count)

what_we_doing_today(my_house, beboere)
