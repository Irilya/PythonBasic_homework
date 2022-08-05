import random


class House:
    """
    Базовый класс, описывающий дом.
    Args:
        money (int) - количество денег в тумбочке (изначально 100)
        food (int) - количество продуктов в холодильнике (изначально 50)
        cat_food (int) - количество продуктов для котов (изначально 30)
        dust (int) - количество пыли в доме (изначально 0)
    """

    def __init__(self, money=100, food=50, cat_food=30, dust=0):
        self.money = money
        self.food = food
        self.cat_food = cat_food
        self.dust = dust

    def __str__(self):
        """
        Метод для получения строкового вида объекта класса Дом.

        :rtype: str
        """
        return f'В доме денег: {self.money}, еды: {self.food}, ' \
               f'кошачей еды: {self.cat_food}, пыли: {self.dust}'


class People:
    """
    Базовый класс, описывающий человека.
    Variable: eaten_food (int) - общее количество съеденой человеком еды
    Args:
        name (str) - имя человека
        house (object class House) - передаются данные объекта Дом, в котором живет человек
        satiety (int) - уровень сытости человека (изначально 30)
        happiness (int) - уровень счастья человека (изначально 100)
    """

    eaten_food = 0

    def __init__(self, name, house, satiety=30, happiness=100):
        self.__name = name
        self.house = house
        self.satiety = satiety
        self.happiness = happiness

    def get_name(self):
        """
        Геттер для получения имени человека.

        :return: __name
        :rtype: str
        """

        return self.__name

    def __str__(self):
        """
        Метод для получения строкового вида объекта класса Человек.

        :rtype: str
        """

        return f'У {self.get_name()} сегодня сытость: {self.satiety}, ' \
               f'уровень счастья: {self.happiness}'

    def petting_the_cat(self):
        """
        Метод, описывающий событие "Гладим кота" и рассчет его последствиц
        :return: self.happiness: (int), self.satiety: (int)
        """

        print(f'{self.get_name()}: Гладим кота. Мур-мур!')
        self.happiness += 5
        self.satiety -= 10
        return self.happiness, self.satiety

    def eat(self):
        """
        Метод для расчета параметров объекта класса человек и связанного с ним класса дом после еды
        :return: self.satiety: (int), self.house.food: (int), self.eaten_food: (int)
        """

        print(f'{self.get_name()}: Что-то кушать хочется! Нум-нум. Вкусно!')
        if self.house.food >= 30:
            self.satiety += 30
            self.house.food -= 30
            self.eaten_food = 30
        else:
            self.satiety += self.house.food
            self.eaten_food = self.house.food
            self.house.food = 0
        return self.satiety, self.house.food, self.eaten_food


class Husband(People):
    """
    Класс Муж. Родительский класс People

    Args:
        name (str) - имя человека
        house (object class House) - передаются данные объекта Дом, в котором живет человек
        satiety (int) - уровень сытости человека (изначально 30)
        happiness (int) - уровень счастья человека (изначально 100)
    """

    def __init__(self, name, house, satiety, happiness):
        super().__init__(name, house, satiety, happiness)

    def work(self):
        """
        Метод для расчета параметров объекта класса Муж и связанного с ним класса Дом после работы
        :return: self.house.money: (int), self.satiety: (int)
        """

        print(f'{self.get_name()}: Пора бы заработать денег. Надо семью кормить.')
        self.house.money += 150
        self.satiety -= 10
        return self.house.money, self.satiety

    def play(self):
        """
        Метод для расчета параметров объекта класса Муж после игры
        :return: self.happiness: (int), self.satiety: (int)
        """

        print(f'{self.get_name()}: Ура! Есть возможность пару каток затащить!')
        self.happiness += 20
        self.satiety -= 10
        return self.happiness, self.satiety


class Wife(People):
    """
    Класс Жена. Родительский класс People

    Args:
        name (str) - имя человека
        house (object class House) - передаются данные объекта Дом, в котором живет человек
        satiety (int) - уровень сытости человека (изначально 30)
        happiness (int) - уровень счастья человека (изначально 100)
    """

    def __init__(self, name, house, satiety, happiness):
        super().__init__(name, house, satiety, happiness)

    def buy_supplies(self):
        """
        Метод для расчета параметров объекта класса Жена и связанного
        с ним класса Дом после покупки продуктов
        :return: self.house.money: (int), self.house.food: (int),
                 self.house.cat_food: (int), self.satiety: (int)
        """

        print(f'{self.get_name()}: Ой! Опять есть нечего! Надо сбегать в магазин.')
        if self.house.cat_food < 20 and self.house.money > 200:
            self.house.cat_food += 30
            self.house.money -= 30
            self.house.food += 50
            self.house.money -= 50
        else:
            self.house.cat_food += 30
            self.house.money -= 30
            self.house.food += self.house.money // 2
            self.house.money = self.house.money // 2
        self.satiety -= 10
        return self.house.money, self.house.food, self.house.cat_food, self.satiety

    def cleaning(self):
        """
        Метод для расчета параметров объекта класса Жена и связанного с ним класса Дом после уборки
        :return: self.house.dust: (int), self.satiety: (int)
        """

        print(f'{self.get_name()}: Надо прибраться, а то развели тут свинарник!')
        if self.house.dust <= 100:
            self.house.dust = 0
        else:
            self.house.dust -= 100
        self.satiety -= 10
        return self.house.dust, self.satiety

    def buy_fur_coat(self):
        """
        Метод для расчета параметров объекта класса Жена и связанного
        с ним класса Дом после покупки шубы
        :return: self.house.money: (int), self.happiness: (int)
        """

        if self.house.money >= 350:
            print(f'{self.get_name()}: Ох, дорогой! Эта шуба - такая прелесть! Я так счастлива!')
            self.house.money -= 350
            self.happiness += 60
        else:
            print(f'{self.get_name()}: Это слишком дорого для нас сейчас!')
        return self.house.money, self.happiness


class Child(People):
    """
    Класс Ребёнок. Родительский класс People

    Args:
        name (str) - имя человека
        house (object class House) - передаются данные объекта Дом, в котором живет человек
        satiety (int) - уровень сытости человека (изначально 30)
        happiness (int) - уровень счастья человека (изначально 100)
        tiredness (int) - уровень усталости человека (изначально 0)
    """

    def __init__(self, name, house, satiety, happiness, tiredness=0):
        super().__init__(name, house, satiety, happiness)
        self.tiredness = tiredness

    def __str__(self):
        """
        Метод переназначен для получения строкового вида объекта класса Ребёнок.

        :rtype: str
        """

        return f'У {self.get_name()} сегодня сытость: {self.satiety}, ' \
               f'уровень счастья: {self.happiness}, усталость: {self.tiredness}'

    def play(self):
        """
        Метод для расчета параметров объекта класса Ребёнок после игры
        :return: self.tiredness: (int), self.satiety: (int), self.happiness: (int)
        """

        print(f'Малыш {self.get_name()} играет и резвится.')
        self.tiredness += 10
        self.satiety -= 10
        self.happiness += 20

    def walk(self):
        """
        Метод для расчета параметров объекта класса Ребёнок после прогулки
        :return: self.tiredness: (int), self.satiety: (int), self.happiness: (int)
        """

        print(f'Малыш {self.get_name()} идет гулять! Можно в парке покататься на карусели.')
        self.tiredness += 10
        self.satiety -= 10
        self.happiness += 20

    def sleep(self):
        """
        Метод для расчета параметров объекта класса Ребёнок после сна
        :return: self.tiredness: (int), self.satiety: (int), self.happiness: (int)
        """

        print(f'Малышу {self.get_name()} пора отдохнуть! Баю-бай.')
        self.tiredness = 0
        self.satiety -= 10
        self.happiness += 10


class Cat:
    """
    Базовый класс Кот, описывающий кота.

    Args:
        name (str) - кличка кота.
        house (object class House) - передаются данные объекта Дом, в котором живет кот
        satiety (int) - уровень сытости человека (изначально 30)
    """

    def __init__(self, name, house, satiety=30):
        self.__name = name
        self.house = house
        self.satiety = satiety

    def get_name(self):
        """
        Геттер для получения имени человека.

        :return: __name
        :rtype: str
        """
        return self.__name

    def __str__(self):
        """
        Метод для получения строкового вида объекта класса Кот.

        :rtype: str
        """

        if self.satiety >= 30:
            return f'Наш {self.get_name()} сегодня сыт! (Сытость {self.satiety})'
        else:
            return f'Наш {self.get_name()} проголодался! (Сытость {self.satiety})'

    def eat(self):
        """
        Метод для расчета параметров объекта класса Кот
        и связанного с ним объекта класса Дом после еды
        :return: self.satiety: (int), self.house.cat_food: (int)
        """

        print(f'Кушай, мой хороший! Кушай, мой {self.get_name()}!')
        if self.house.cat_food >= 10:
            self.satiety += 20
            self.house.cat_food -= 10
        else:
            self.satiety += self.house.cat_food * 2
            self.house.cat_food = 0
        return self.satiety, self.house.cat_food

    def sleep(self):
        """
        Метод для расчета параметров объекта класса Кот
        и связанного с ним объекта класса Дом после сна
        :return: self.satiety: (int)
        """

        print(f'Тсссс! Наш {self.get_name()} спит!')
        self.satiety -= 10
        return self.satiety

    def tears_wallpaper(self):
        """
        Метод для расчета параметров объекта класса Кот
        и связанного с ним объекта класса Дом после события "драть обои"
        :return: self.house.dust: (int), self.satiety: (int)
        """

        print(f'Ах, негодник {self.get_name()}! Опять все обои подрал!')
        self.house.dust += 5
        self.satiety -= 10
        return self.house.dust, self.satiety


def family_life(house, husband, wife, child, cats):
    """
    Функция, описывающая изменения состояний объектов классов и их действия
    при изменении тех или иных параметров.
    :param house: object class House()
    :param husband: object class Husband(People)
    :param wife: object class Wife(People)
    :param child: object class Child(People)
    :param cats: list of objects class Cat()
    :return: earned_money: (int), eaten_food: (int), fur_coat: (int)
    """
    global fur_coat
    global earned_money
    global eaten_food
    print(house)
    print(husband)
    print(wife)
    print(child)
    for i_cat in cats:
        print(i_cat)
    house.dust += 5
    if husband.satiety < 30 and house.food > 0:
        husband.happiness -= 10
        husband.eat()
        eaten_food += husband.eaten_food
    elif house.money < 100:
        husband.happiness -= 20
        husband.work()
        earned_money += 150
    elif husband.happiness == 10:
        husband.play()
    elif house.money > 350:
        husband.play()
    else:
        husband.work()
        earned_money += 150

    if wife.satiety < 30 and house.food > 0:
        wife.eat()
        eaten_food += wife.eaten_food
    elif house.food < 50 or house.cat_food < 20 and house.money > 0:
        wife.buy_supplies()
    elif wife.happiness <= 20:
        if house.money >= 350:
            wife.buy_fur_coat()
            fur_coat += 1
        else:
            wife.petting_the_cat()
    elif house.dust >= 90:
        husband.happiness -= 10
        wife.happiness -= 10
        child_.happiness -= 10
        wife.petting_the_cat()
        if house.dust > 150:
            wife.cleaning()
    else:
        wife.petting_the_cat()

    if child.satiety < 30 and house.food > 0:
        child.happiness -= 10
        child.eat()
        eaten_food += child.eaten_food
    elif child.tiredness > 30:
        child.sleep()
    elif child.happiness < 20:
        child.play()
    else:
        choice = random.randint(1, 3)
        if choice == 1:
            child.play()
        else:
            child.walk()

    for i_cat in cats:
        if i_cat.satiety < 20 and house.cat_food > 0:
            i_cat.eat()
        else:
            choice = random.randint(1, 3)
            if choice == 1:
                i_cat.sleep()
            else:
                i_cat.tears_wallpaper()

    return earned_money, eaten_food, fur_coat


my_house = House()
husband_ = Husband('Пётр Иванович', my_house, satiety=30, happiness=100)
wife_ = Wife('Матрёна Феоктисовна', my_house, satiety=30, happiness=100)
child_ = Child('Петруша', my_house, satiety=30, happiness=100, tiredness=0)
my_cats = []
cat_1 = Cat('Пусик', my_house, satiety=30)
my_cats.append(cat_1)
cat_2 = Cat('Масик', my_house, satiety=30)
my_cats.append(cat_2)
cat_3 = Cat('Кактус', my_house, satiety=30)
my_cats.append(cat_3)
day_count = 0
fur_coat = 0
earned_money = 0
eaten_food = 0
day = 0
while day_count < 365:
    day_count += 1
    if husband_.satiety <= 0:
        print('Вы довели своего кормильца до истощения! Ваш муж умер!')
        day_count = 365
        break
    elif husband_.happiness < 10:
        print('Вы довели своего кормильца до нервного истощения! Ваш муж умер от депрессии!')
        day_count = 365
        break
    elif wife_.satiety <= 0:
        print('Как можно так измываться над бедной женщиной! Ваша жена погибла от истощения!')
        day_count = 365
        break
    elif child_.satiety <= 0:
        print('Жестокие родители! Вы уморили ребенка голодом! Полиция уже едет!')
        day_count = 365
        break
    elif wife_.happiness < 10:
        print('Как можно так измываться над бедной женщиной! Ваша жена погибла от глубокой депрессии!')
        day_count = 365
        break
    elif child_.happiness < 10:
        print('У ребенка тяжелая депрессия! Срочно в реанимацию!')
        day_count = 365
        break
    elif child_.tiredness > 40:
        print('Тяжелое переутомление у ребенка! Скорую! Срочно!')
        day_count = 365
        break
    for cat in my_cats:
        if cat.satiety <= 0:
            print(f'Ваш питомец {cat.get_name()} погиб от истощения! Защитники животных внесли вас в черный список!')
            day_count = 365
            break
    else:
        print(f'\nДень {day_count}')
        day = day_count
        family_life(my_house, husband_, wife_, child_, my_cats)


print(f'\nЗа {day} дней:\nзаработано денег {earned_money}, \nсъедено еды {eaten_food}, \nкуплено шуб: {fur_coat}')
