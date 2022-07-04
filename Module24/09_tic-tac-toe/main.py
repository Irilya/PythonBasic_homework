

class Cell:

    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value == 'null':
            return f'|_0_|'
        elif self.value == 'cross':
            return f'|_X_|'
        else:
            return f'|___|'


class Board:

    def __init__(self, row):
        self.row = row
        self.board = []

    def get_board(self):

        for _ in range(self.row):
            i_row = []
            for _ in range(self.row):
                cell = Cell()
                i_row.append(cell)
            self.board.append(i_row)
        return self.board

    def show_board(self):

        for i in range(self.row):
            print('   ', i + 1, end='')
        print()
        str = 1
        for i_row in self.board:
            print(str, end='')
            for j in i_row:
                print(j, end='')
            str += 1
            print()


class Player:

    def __init__(self, name, suit, win=0):
        self.name = name
        self.suit = suit
        self.win = win


def get_my_board():   #  Создание пустой доски

    print('Добро пожаловать в игру!')
    while True:
        try:
            board_row = int(input('Введите сторону игрового поля (от 3 до 10) '))
            if board_row in range(3, 11):
                break
            else:
                print('Неверно задан параметр. Введите цифру от 3 до 10')
        except ValueError:
            print('Неверно задан параметр. Введите цифру от 3 до 10')

    my_board = Board(board_row)
    my_board.get_board()
    my_board.show_board()

    return my_board


def win_status(board, player):  # Прописываем условия победы

    value = player.suit
    if all([(board.board[0][j]).value == value for j in range(board.row)]) \
            or all([(board.board[1][j]).value == value for j in range(board.row)]) \
            or all([(board.board[2][j]).value == value for j in range(board.row)]) \
            or all([(board.board[i][0]).value == value for i in range(board.row)]) \
            or all([(board.board[i][1]).value == value for i in range(board.row)]) \
            or all([(board.board[i][2]).value == value for i in range(board.row)]) \
            or all([(board.board[i][i]).value == value for i in range(board.row)]) \
            or all([(board.board[i][board.row - i - 1]).value == value for i in range(board.row)]):
        print(f'{player.name}! Вы победили!!!')
        player.win += 1
        return True
    return False


def get_choice(players):   # После окончания игры предлагаем повторить, при этом игроки меняются фишками

    while True:
        try:
            choice = input(f'{players[0].name}, {players[1].name}, хотите продолжить? y/n ')
            if choice in ['y', 'n']:
                break
            else:
                print(f'не понял, так вы хотите продолжить? y/n ')
        except ValueError:
            print(f'не понял, так вы хотите продолжить? y/n ')
    if choice == 'y':
        my_board = get_my_board()
        players[0], players[1] = players[1], players[0]
        players[0].suit = 'cross'
        players[1].suit = 'null'
        print(f'{players[0].name}! Вы играете крестиками.')
        print(f'{players[1].name}! Вы играете ноликами.')
        start_play(my_board, players)
    else:
        print(f'Ваши результаты:\n{players[0].name}: количество побед: {players[0].win}'
              f'\n{players[1].name}: количество побед: {players[1].win}'
              f'\nДо новых встреч!')


def get_players():   # Создание первоначального списка игроков для использования в последующих турах

    players = []
    name_1 = input('Введите имя первого игрока: ')
    name_2 = input('Введите имя второго игрока: ')
    player_1 = Player(name_1, suit='cross')
    print(f'{player_1.name}! Вы играете крестиками.')
    player_2 = Player(name_2, suit='null')
    print(f'{player_2.name}! Вы играете ноликами.')
    players.append(player_1)
    players.append(player_2)
    return players


def start_play(board, players):  # Начало игры. Прописываем условия для вызова нужного игрока

    step_count = 1
    while step_count <= board.row ** 2:
        if step_count % 2:
            play_step(board, players[0])
            if step_count > 5:
                if win_status(board, players[0]):
                    get_choice(players)
                    break
                break
            step_count += 1
        else:
            play_step(board, players[1])
            if step_count > 6:
                if win_status(board, players[1]):
                    get_choice(players)
                    break
                break
            step_count += 1
    else:
        print('Ничья! Сильная игра!')
        get_choice(players)


def play_step(board, player):  # Игровые действия для каждого хода. Проверка ввода

    value = player.suit
    print(f'\n{player.name}, Ваш ход!')
    while True:
        try:
            coordinate_i = int(input(f'{player.name}! На какую клетку пойдете? Введите номер строки. '
                                     f'(цифра от 1 до {board.row}): '))
            if coordinate_i in range(1, board.row + 1):
                break
            else:
                print(f'Неверное значениe! Введите номер строки. (цифра от 1 до {board.row})')
        except ValueError:
            print(f'Неверное значениe! Введите номер строки. (цифра от 1 до {board.row})')
    while True:
        try:
            coordinate_j = int(input(f'{player.name}! Введите номер колонки. (цифра от 1 до {board.row}): '))
            if coordinate_j in range(1, board.row + 1):
                break
            else:
                print(f'Неверное значениe! Введите номер колонки. (цифра от 1 до {board.row})')
        except ValueError:
            print(f'Неверное значениe! Введите номер колонки. (цифра от 1 до {board.row})')
    if board.board[coordinate_i - 1][coordinate_j - 1].value is None:
        board.board[coordinate_i - 1][coordinate_j - 1] = Cell(f'{value}')
        board.show_board()
    else:
        print('Клетка занята')
        play_step(board, player)


board_1 = get_my_board()
my_players = get_players()
start_play(board_1, my_players)
