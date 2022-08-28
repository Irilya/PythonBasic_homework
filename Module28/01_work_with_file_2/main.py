import typing


class File:
    """
    Контекст-менеджер для работы с файлами. Если файла не существует, то он создается,
    иначе файл открывается, совершаются необходимые действия с ним, файл закрывается.
    Ошибки, в случае их возникновения, обрабатываются, проверяется правильность ввода
    аргумента для действий с файлом.
    """
    MODE = ['r', 'w', 'rb', 'wb', 'r+', 'rb+', 'w+', 'wb+', 'a', 'a+', 'ab', 'ab+']

    def __init__(self, file_name: str, access_mode: str) -> None:
        self.file_name = file_name
        self.access_mode = access_mode
        self.file_obj = None

    def __enter__(self) -> typing.IO:
        """
        Функция для открытия файла с проверкой правильности ввода аргумента для действий с файлом.
        :return: typing.IO
        """
        while self.access_mode not in self.MODE:
            print('Ошибка ввода')
            self.access_mode = input('Введите корректное значение аргумента для открытия файла. '
                                     '(r, w, rb, wb, r+, rb+, w+, wb+, a, a+, ab, ab+): ')
        else:
            try:
                self.file_obj = open(self.file_name, self.access_mode)
            except FileNotFoundError:
                self.file_obj = open(self.file_name, 'w+')

        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        Функция закрывает файл после работы с ним. Обрабатывает исключения.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: bool
        """
        if exc_type is not None:
            print(f'{exc_type}: {exc_val}\n{exc_tb}')
        self.file_obj.close()
        return True


# with File('test.txt', 'r') as f:
#     print(f.read())
# with File('test.txt', 'a') as f:
#     f.write('This is line1\nThis is line2\nThis is line3\n')
# with File('test.txt', 'r') as f:
#     f.undifined()
# with File('test.txt', '1') as f:
#     print(f.readline())
