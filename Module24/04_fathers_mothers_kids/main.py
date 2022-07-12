import random


list_not_calm = ['Пора переодеть ребёнка', 'Ребёнок устал', 'Ребёнок хочет поиграть']


class Parent:

    def __init__(self, name, age, child_list=[]):
        self.name = name
        self.age = age
        try:
            self.child_list = list(child_list)
        except TypeError:
            self.child_list.append(child_list)

    def info_parent(self):

        print('Имя родителя: {}, возраст родителя: {}, дети: {}'.format(
            self.name, self.age, ', '.join(self.child_list)
            ))

    def feed_the_baby(self, child):

        print('Моё солнышко проголодалось! Кушай, радость моя!')
        child.hunger = False
        print('Ребёнок наелся.')
        return child.hunger

    def calm_the_child_down(self, child, calm):

        if calm == 'Пора переодеть ребёнка':
            print('Вот мы и переоделись! Теперь нам удобно и тепло!')
            child.calmness = True
        elif calm == 'Ребёнок устал':
            print('Пора спать! Баю-бай. Пусть тебе приснится рааай!'
                  'Полон ласковых горииилл. И нильский крокодил.')
            child.calmness = True
        elif calm == 'Ребёнок хочет поиграть':
            print('Поиграем в прятки. Раз, два, три, четыре, пять, я иду тебя искать')
            child.calmness = True
        return child.calmness


class Child:

    def __init__(self, name, age, calmness=False, hunger=True):
        self.name = name
        self.age = age
        self.calmness = calmness
        self.hunger = hunger

    def age_verification(self, parent):

        if (parent.age - self.age) < 16:
            print(f'{self.name} - Неправильно задан возраст')
            self.age = int(input('Хотите исправить? '))
            Child.age_verification(self, parent)
        else:
            Child.info_child(self)

    def info_child(self):

        print('Имя ребёнка: {}, возраст ребёнка: {}'.format(
            self.name, self.age
            ))
        if self.hunger is True:
            print('Ребёнок голоден')
        else:
            print('Ребёнок сыт')
        if self.calmness is False:
            print('Ребёнок капризничает')
        else:
            print('Ребёнок спокоен')

    def baby_calmness(self):

        if self.calmness is False:
            calm = random.choice(list_not_calm)
            print(calm)
            return calm
        else:
            print('Ребёнок спокоен')


def whom_feed():

    choice = input('Кого покормим? 1 - Аня, 2 - Юра, 3 - Рома, 0 - Выход ')
    while choice != '0':
        if choice == '1':
            if daughter.hunger is True:
                maman.feed_the_baby(daughter)
            else:
                print('Ребёнок сыт')
        elif choice == '2':
            if son_1.hunger is True:
                maman.feed_the_baby(son_1)
            else:
                print('Ребёнок сыт')
        elif choice == '3':
            if son_2.hunger is True:
                maman.feed_the_baby(son_2)
            else:
                print('Ребёнок сыт')
        elif choice == '0':
            break
        else:
            print('Кого вы имеете ввиду? ')
        choice = input('Кого покормим? 1 - Аня, 2 - Юра, 3 - Рома, 0 - Выход ')


def whom_care():

    choice = input('Кто у нас тут капризничает? 1 - Аня, 2 - Юра, 3 - Рома, 0 - Выход ')
    while choice != '0':
        if choice == '1':
            if daughter.calmness is False:
                calm = daughter.baby_calmness()
                maman.calm_the_child_down(daughter, calm)
            else:
                print('Ребёнок спокоен')
        elif choice == '2':
            if son_1.calmness is False:
                calm = son_1.baby_calmness()
                maman.calm_the_child_down(son_1, calm)
            else:
                print('Ребёнок спокоен')
        elif choice == '3':
            if son_2.calmness is False:
                calm = son_2.baby_calmness()
                maman.calm_the_child_down(son_2, calm)
            else:
                print('Ребёнок спокоен')
        elif choice == '0':
            break
        else:
            print('Кого вы имеете ввиду? ')
        choice = input('Кто у нас тут капризничает? 1 - Аня, 2 - Юра, 3 - Рома, 0 - Выход ')


list_child = []
daughter = Child('Аня', 2)
son_1 = Child('Юра', 5)
son_2 = Child('Рома', 15, False, False)

maman = Parent('Мария Сергеевна Иванова', 28, (son_1.name, son_2.name, daughter.name))
papa = Parent('Пётр Александрович Иванов', 30, (son_1.name, son_2.name, daughter.name))
maman.info_parent()
papa.info_parent()
daughter.age_verification(maman)
son_1.age_verification(maman)
son_2.age_verification(maman)
whom_feed()
whom_care()
