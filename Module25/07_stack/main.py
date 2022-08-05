class Stack:
    """
    Базовый класс Stack, как абстрактный тип данных,
    представляющий собой список элементов, организованных по принципу LIFO
    self.__stack (list) - список для хранения данных
    """

    def __init__(self):
        self.__stack = []

    def __str__(self):
        return ', '.join(self.__stack)

    def emptylist(self):
        """
        Метод полного очищения списка данных
        :return: self.__stack: (list)
        """

        self.__stack = []
        return self.__stack

    def push(self, item):
        """
        Метод добавления элементов в список данных

        """

        self.__stack.append(item)

    def pop(self):
        """
        Метод удаления последнего элемента из списка данных

        :return: self.__stack.pop(): (list[-1])
        """
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()


class TaskManager:
    """
    Базовый класс Менеджер задач сортирует задачи по приоритету в виде стеков задач
    self.task: (dict) - словарь, в котором формируются стеки задач по приоритету
    """

    def __init__(self):
        self.task = dict()

    def __str__(self):
        """
        Метод для получения строкового вида объекта класса TaskManager.

        :rtype: list[str]
        """
        info = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                info.append('{prior} - {task}\n'.format(
                    prior=str(i_priority),
                    task=self.task[i_priority]
                    )
                )
        return ''.join(info)

    def new_task(self, elem, priority):
        """
        Метод, формирующий стеки задач для каждого уроня приоритета
        :param elem:
        :param priority: (int)
        """

        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(elem)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# Без подсказки не справилась. Понятно отдельно про стек, отдельно про менеджер.
# Что можно создать объект класса внутри другого класса в голову не пришло.(
