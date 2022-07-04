import random


class Warrior:

    def __init__(self, helth=100, choice=0):

        self.helth = helth
        self.choice = choice


Ork = Warrior()
Elf = Warrior()


def battle():
    while Ork.helth > 0 and Elf.helth > 0:
        Warrior.choice = random.randint(0, 2)
        if Warrior.choice == 0:
            print('Орк пошел в атаку на Эльфа')
            Elf.helth -= 20
            print('У Эльфа осталось {} очков здоровья'.format(Elf.helth))
        else:
            print('Эльф пошел в атаку на Орка')
            Ork.helth -= 20
            print('У Орка осталось {} очков здоровья'.format(Ork.helth))
    else:
        if Ork.helth == 0:
            print('Воин Орк погиб смертью храбрых!')
        else:
            print('Воин Эльф погиб смертью храбрых!')


battle()
