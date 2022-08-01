class Node:
    """
    Класс для создания узла в списке
    Args:
        data - передаются данные для узла. Могут быть разных типов.
    Variable:
        nextnode - ссылка на следующий узел последовательности.
    """
    def __init__(self, data) -> None:
        self.data = data
        self.nextnode = None


class LinkedList:
    """
    Класс односвязного списка.
    Variable:
       head - обозначает с какого узла начинается обход списка
    """
    def __init__(self):
        self.head = None

    def ll_print(self) -> None:
        """
        Метод для визуализации списка
        :return:
        """
        headnode = self.head
        print(f'\nОдносвязный список')
        print('=====================')
        while headnode is not None:
            print(headnode.data)
            headnode = headnode.nextnode
        print(f'=====================\n')

    def add_node_in_end(self, newdata):
        """
        Метод для добавления нового узла в конец списка
        и создания новой ссылки на последний узел
        :param newdata:
        :return:
        """
        node = Node(newdata)
        if self.head is None:
            self.head = node
            return
        lastnode = self.head
        while lastnode.nextnode:
            lastnode = lastnode.nextnode
        lastnode.nextnode = node

    def contains(self, node):
        """
        Метод позволяет найти нужный узел по значению при обходе списка
        :param: node
        :return: True or False (bool)
        """
        lastnode = self.head
        while lastnode:
            if lastnode.data == node:
                return True
            else:
                lastnode = lastnode.nextnode
        return False

    def get_id_node(self, nodeid: int):
        """
        Метод позволяет найти нужный узел по индексу(номеру) положения в списке
        :param: nodeid (int)
        :return: lastnode.data (значение узла с заданным номером)
        """
        lastnode = self.head
        count_id = 1
        while lastnode:
            if count_id < nodeid:
                lastnode = lastnode.nextnode
                count_id += 1
            elif count_id == nodeid:
                return lastnode.data
            else:
                print('Неверно заданы параметры')

    def remove_node(self, rdata):
        """
        Метод удаляет узел по значению и переназначает связи узлов в списке
        :param: rdata
        :return: новый список с измененными связями
        """
        headnode = self.head
        lastnode = None
        if headnode is not None:
            if headnode.data == rdata:
                self.head = headnode.nextnode
                return
        while headnode is not None:
            if headnode.data == rdata:
                break
            lastnode = headnode
            headnode = headnode.nextnode
        if headnode is None:
            return
        lastnode.nextnode = headnode.nextnode


my_list = LinkedList()
my_list.add_node_in_end('Булинь')
my_list.add_node_in_end('Восьмерка')
my_list.add_node_in_end('Шкотовый')
my_list.add_node_in_end('Прямой штык')

my_list.ll_print()
print(my_list.contains('Восьмерка'))
print(my_list.contains('Во'))
print(my_list.get_id_node(3))
my_list.remove_node('Восьмерка')
my_list.ll_print()
