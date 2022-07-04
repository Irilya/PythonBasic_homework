class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):

        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True


class Gardener:

    def __init__(self, name, potato_garden):

        self.name = name
        self.potato_garden = potato_garden

    def garden_care(self):

        print(f'Садовник {self.name} поливает грядку.')
        self.potato_garden.grow_all()

    def harvesting(self):

        print('Ура! Собираем урожай!\nУрожай собран. Грядки опустели.\n')
        for i_potato in self.potato_garden.potatoes:
            i_potato.state = 0
        if self.potato_garden.are_all_ripe() is not True:
            choice = input('Засеем грядку снова? да/нет ')
            if choice == 'да':
                count = int(input('Сколько сеем картофелин? '))
                self.potato_garden = PotatoGarden(count)
                self.potato_garden.are_all_ripe()
                while self.potato_garden.are_all_ripe() is not True:
                    my_gardener.garden_care()
                else:
                    my_gardener.harvesting()

            else:
                print('Зима пришла. Ждем весны')


my_garden = PotatoGarden(5)
my_gardener = Gardener('Пол', my_garden)
my_garden.are_all_ripe()
while my_garden.are_all_ripe() is not True:
    my_gardener.garden_care()
else:
    my_gardener.harvesting()
