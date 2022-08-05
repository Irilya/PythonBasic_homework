class Property:
    """
    Базовый класс, описывающий имущество человека

    Args:
        worth (float) - передается стоимость имущества

    Variable:
        tax (float) - сюда записывается значение налога на имущество
    """
    def __init__(self, worth):
        self.worth = worth
        self.tax = None

    def get_tax(self):
        """
        Метод для получения значения налога на имущество

        :return: tax
        :rtype: float
        """
        return self.tax


class Apartment(Property):
    """
    Класс Apartment. Родитель: Property.

    Args:
        worth (float) - передается стоимость имущества

    Variable:
        tax (float) - сюда записывается значение налога на имущество
    """

    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Метод для получения значения налога на дом

        :return: tax
        :rtype: float
        """

        self.tax = self.worth / 1000
        return self.tax


class Car(Property):
    """
    Класс Car. Родитель: Property.

    Args:
        worth (float) - передается стоимость имущества

    Variable:
        tax (float) - сюда записывается значение налога на имущество
    """

    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Метод для получения значения налога на машину

        :return: tax
        :rtype: float
        """

        self.tax = self.worth / 200
        return self.tax


class CountryHouse(Property):
    """
    Класс CountryHouse. Родитель: Property.

    Args:
        worth (float) - передается стоимость имущества

    Variable:
        tax (float) - сюда записывается значение налога на имущество
    """
    def __init__(self, worth):
        super().__init__(worth)

    def get_tax(self):
        """
        Метод для получения значения налога на загородный дом

        :return: tax
        :rtype: float
        """

        self.tax = self.worth / 500
        return self.tax


def tax_calculation():

    while True:
        try:
            worth = float(input('\nВведите стоимость Вашего основного жилья: '))
            if type(worth) is float:
                break
        except ValueError:
            print('\nНеверно введены данные. Введите сумму цифрами.')

    appartment = Apartment(worth)

    while True:
        try:
            worth = float(input('\nВведите стоимость Вашего автомобиля: '))
            if type(worth) is float:
                break
        except ValueError:
            print('\nНеверно введены данные. Введите сумму цифрами.')

    car = Car(worth)

    while True:
        try:
            worth = float(input('\nВведите стоимость Вашего загородного дома: '))
            if type(worth) is float:
                break
        except ValueError:
            print('\nНеверно введены данные. Введите сумму цифрами.')

    countryhouse = CountryHouse(worth)

    tax = appartment.get_tax() + car.get_tax() + countryhouse.get_tax()
    tax = round(tax, 2)
    return tax


def cash_level(tax):

    while True:
        try:
            cash = float(input('\nВведите количество денег на Вашем счету: '))
            if type(cash) is float:
                break
            else:
                print('\nНеверно введены данные. Введите сумму цифрами.')
        except ValueError:
            print('\nНеверно введены данные. Введите сумму цифрами.')

    print(f'\nНалог на Ваше имущество составил: {tax}')
    if cash < tax:
        dif = tax - cash
        print(f'\nНа Вашем счету не хватает средств для погашения налоговой задолженности. '
              f'Необходимо еще {dif} руб.')
    else:
        cash -= tax
        print(f'\nНалоговая задолженность погашена. Остаток на счету: {cash} руб')


my_tax = tax_calculation()
cash_level(my_tax)

