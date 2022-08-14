class Date:
    """Класс Date должен:
     - проверять числа даты на корректность;
     - конвертировать строку даты в объект класса Date, состоящий из
       соответствующих числовых значений дня, месяца и года.
    """
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

    @classmethod
    def from_string(cls, date_string: str) -> 'Date':
        """
        Метод класса конвертирует строку даты в объект класса Date, состоящий из
        соответствующих числовых значений дня, месяца и года.
        :param date_string: str
        :return: 'Date'
        """
        cls.date_string = date_string
        day, month, year = map(int, date_string.split('-'))
        date_ = cls(day, month, year)
        return date_

    @classmethod
    def is_date_valid(cls, date_string: str) -> bool:
        """
        Метод класса проверяeт числа даты на корректность
        """
        day, month, year = map(int, date_string.split('-'))
        if 0 < year <= 9999 and month != 2:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                if day in range(1, 32):
                    return True
                else:
                    print('Нет такого дня в этом месяце.')
                    return False
            elif month in [4, 6, 9, 11]:
                if day in range(1, 31):
                    return True
                else:
                    print('Нет такого дня в этом месяце.')
                    return False
            else:
                print('Нет такого месяца в году.')
                return False
        elif 0 < year <= 9999 and month == 2:
            if year % 4 == 0 and year % 100 != 0 \
                    or year % 100 == 0 and year % 400 == 0:
                if day in range(1, 30):
                    return True
                else:
                    print('Нет такого дня в этом месяце.')
                    return False
            else:
                if day in range(1, 29):
                    return True
                else:
                    print('Нет такого дня в этом месяце.')
                    return False
        else:
            print('Нет такой даты.')
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('31-06-1900'))
