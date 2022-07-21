

class Person:
    """
    Базовый класс, описывающий человека.
    Args:
        name (str) - передается имя человека
        surname (str) - передается фамилия человека
        age (int) - передается возраст человека

    """

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        """
        Метод для получения строкового вида объекта класса.

        :rtype: str
        """

        return f'Имя: {self.__name}\tФамилия: {self.__surname}\tВозраст: {self.__age}'

    def get_name(self):
        """
        Геттер для получения имени человека.

        :return: __name
        :rtype: str
        """

        return self.__name

    def get_surname(self):
        """
        Геттер для получения фамилии человека.

        :return: __surname
        :rtype: str
        """

        return self.__surname

    def get_age(self):
        """
        Геттер для получения возраста человека.

        :return: __age
        :rtype: int
        """

        return self.__age

    def set_age(self, age):
        """
        Сеттер для установления возраста человека
        :param age: возраст
        :type: int
        :raise Exception: если возраст не в границах от 1 до 99, то вызывается исключение
        """

        if age in range(1, 99):
            self.__age = age
        else:
            raise Exception('Недопустимое значение.')


class Employee(Person):
    """
    Класс Employee. Родительский класс Person.
    Args:
        name (str) - передается имя работника
        surname (str) - передается фамилия работника
        age (int) - передается возраст работника
        salary (float) - передается оклад работника

    """

    def __init__(self, name, surname, age, salary=0):
        super().__init__(name, surname, age)
        self.salary = salary

    def __str__(self):
        return f'Работник {self.get_surname()} {self.get_name()}, заработная плата: {self.salary}'

    def calculation_salary(self):
        """
        Метод для получения размера заработной платы
        :return: self.salary
        :rtype: float
        """

        return self.salary


class Manager(Employee):
    """
    Класс Manager. Родительский класс Employee.
    Args:
        name (str) - передается имя менеджера
        surname (str) - передается фамилия менеджера
        age (int) - передается возраст менеджера
        salary (float) - передается оклад менеджера

    """

    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age, salary)

    def calculation_salary(self):
        """
        Метод для получения размера заработной платы
        :return: self.salary
        :rtype: float
        """

        return self.salary


class Agent(Employee):
    """
    Класс Agent. Родительский класс Employee.
    Args:
        name (str) - передается имя менеджера
        surname (str) - передается фамилия менеджера
        age (int) - передается возраст менеджера
        salary (float) - передается оклад менеджера
        sales (float) - передается объем продаж

    """

    def __init__(self, name, surname, age, salary, sales):
        super().__init__(name, surname, age, salary)
        self.sales = sales

    def calculation_salary(self):
        """
        Метод для получения размера заработной платы
        :return: self.salary
        :rtype: float
        """

        self.salary = self.salary + self.sales * 0.05
        return self.salary

    def __str__(self):
        """
        Метод переназначен для получения строкового вида объекта класса Agent.

        :rtype: str
        """

        return f'Работник {self.get_surname()} {self.get_name()}, ' \
               f'заработная плата: {self.calculation_salary()}'


class Worker(Employee):
    """
    Класс Agent. Родительский класс Employee.
    Args:
        name (str) - передается имя менеджера
        surname (str) - передается фамилия менеджера
        age (int) - передается возраст менеджера
        hours (int) - передается количество отработанных часов
    """

    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def calculation_salary(self):
        """
        Метод для получения размера заработной платы
        :return: self.salary
        :rtype: float
        """

        self.salary = self.hours * 155.3
        self.salary = round(self.salary, 2)
        return self.salary

    def __str__(self):
        """
        Метод переназначен для получения строкового вида объекта класса Agent.

        :rtype: str
        """

        return f'Работник {self.get_surname()} {self.get_name()}, ' \
               f'заработная плата: {self.calculation_salary()}'


employee_list = []

manager_1 = Manager('Петр', 'Сидоров', 45, 45000)
employee_list.append(manager_1)
manager_2 = Manager('Александр', 'Кораблев', 42, 40000)
employee_list.append(manager_2)
manager_3 = Manager('Марк', 'Давидович', 35, 40000)
employee_list.append(manager_3)
agent_1 = Agent('Алексей', 'Сидоров', 28, 25000, 40000)
employee_list.append(agent_1)
agent_2 = Agent('Алексей', 'Ковров', 25, 25000, 50000)
employee_list.append(agent_2)
agent_3 = Agent('Вениамин', 'Ковров', 23, 20000, 35000)
employee_list.append(agent_3)
worker_1 = Worker('Иван', 'Петров', 32, 175)
employee_list.append(worker_1)
worker_2 = Worker('Илья', 'Торонтов', 45, 172)
employee_list.append(worker_2)
worker_3 = Worker('Никита', 'Королев', 27, 177)
employee_list.append(worker_3)


print(f'{manager_1}\n{manager_2}\n{manager_3}\n{agent_1}\n{agent_2}\n{agent_3}\n{worker_1}\n{worker_2}\n{worker_3}')
print('Заработная плата:')
for item in employee_list:
    print(item.calculation_salary())
