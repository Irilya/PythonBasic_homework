import random


ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['hearts', 'diamonds', 'clubs', 'spades']
max_chip_balance = 10000
max_count_players = 8


class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.ishidding = False

    def __repr__(self):
        if self.ishidding is True:
            return f'[<X>]'
        else:
            return f'[**{self.rank}** {self.suit}]'

    def is_ace(self):
        if self.rank == 'A':
            return True


class CardsDeck:

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards.pop(0)
        return card


class Player:

    def __init__(self, name, bet, chip_balance, player_cards=[], play_status=False):

        self.name = name
        self.bet = bet
        self.chip_balance = chip_balance
        self.player_cards = player_cards
        self.play_status = play_status
        self.isbankrupt = False

    def add_card(self, card):

        self.player_cards.append(card)
        return self.player_cards

    def get_value(self):

        aces = 0
        value_aces = 0
        for card in self.player_cards:
            if card.rank in ('K', 'Q', 'J'):
                value_aces += 10
            elif card.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                value_aces += int(card.rank)
            if card.is_ace():
                aces += 1
                value_aces += 11
        while (value_aces > 21) and aces > 1:
            value_aces -= 10
            aces -= 1
        return value_aces

    def hit(self, card):

        print("Сдаю...\n")
        self.add_card(card)
        return self.player_cards

    def stand(self):

        print(f'{self.name}: Достаточно!\n')
        self.play_status = True

    def check_bankrupt(self):

        if self.get_value() > 21:
            self.isbankrupt = True

    def check_bj(self):

        if self.get_value() == 21 and len(self.player_cards) == 2:
            return True
        else:
            return False


def new_players_list(players):  # Определяем новый список игроков при каждом новом туре

    new_players = []
    for i_player in players:
        while True:
            try:
                choice = input(f'{i_player.name}, хотите продолжить? y/n ')
                if choice in ['y', 'n']:
                    break
                else:
                    print(f'{i_player.name},не понял, так вы хотите продолжить? y/n ')
            except ValueError:
                print(f'{i_player.name},не понял, так вы хотите продолжить? y/n ')
        if choice == 'y':
            if i_player.chip_balance > 0:
                while True:
                    try:
                        bet = int(input(f'{i_player.name}. Ваша ставка? (10, 20, 50, 100) '))
                        if bet in [10, 20, 50, 100]:
                            break
                        else:
                            print('Неправильный размер ставки! Ставка: (10, 20, 50, 100) ')
                    except ValueError:
                        print('Неправильный размер ставки! Ставка цифрами: (10, 20, 50, 100) ')
                i_player = Player(i_player.name, bet, i_player.chip_balance, play_status=False)
                i_player.chip_balance -= i_player.bet
                new_players.append(i_player)
        else:
            pass

    return new_players


def new_play(players, deck, croupier):   # запуск нового тура

    new_players = new_players_list(players)
    croupier.player_cards = []
    croupier.isbankrupt = False
    croupier.play_status = False
    if len(new_players) > 0:
        start_game(new_players, deck, croupier)
    else:
        print('До новых встреч!')


def get_players():  # Получение первоначального списка при старте игры, контроль данных при введении

    players = []
    deck = CardsDeck()
    croupier = Player(name='Croupier', bet=10, chip_balance=50000, play_status=False)
    print('Добро пожаловать в наш Клуб!')
    while True:
        try:
            count_players = int(input('Сколько игроков примут участие в игре? '))
            if count_players in range(1, 9):
                break
            else:
                print('Неверное количество игроков. Введите цифру от 1 до 8.')
        except ValueError:
            print('Неверное количество игроков. Введите цифру от 1 до 8.')
    print('Делаем ставки!')
    for i_player in range(1, count_players + 1):
        name = f'Игрок {i_player}'
        while True:
            try:
                chip_balance = int(input(f'{name}. Введите Ваш баланс (от 100 до 10000): '))
                if chip_balance in range(100, 10001):
                    break
                else:
                    print('Неверное значение! Введите Ваш баланс (от 100 до 10000): ')
            except ValueError:
                print('Неверное значение! Введите Ваш баланс цифрами (от 100 до 10000): ')
        while True:
            try:
                bet = int(input(f'{name}. Ваша ставка? (10, 20, 50, 100) '))
                if bet in [10, 20, 50, 100]:
                    break
                else:
                    print('Неправильный размер ставки! Ставка: (10, 20, 50, 100) ')
            except ValueError:
                print('Неправильный размер ставки! Ставка цифрами: (10, 20, 50, 100) ')
        i_player = Player(name, bet, chip_balance, player_cards=[], play_status=False)
        players.append(i_player)
        i_player.chip_balance -= i_player.bet

    return players, deck, croupier


def croupier_bankrupt(players, croupier):   # Наступление случая "перебор у крупье"

    croupier.player_cards[0].ishidding = False
    print(f'Открываем карты! Набрано {croupier.get_value()} '
          f'очков: {croupier.player_cards}. Перебор!\n')
    for i_player in players:
        if i_player.get_value() <= 21:
            i_player.chip_balance += i_player.bet * 1.5
            print(f'{i_player.name}, у вас {i_player.get_value()} очков! '
                  f'Вы победили! Ваш баланс: {i_player.chip_balance}\n')


def all_pass(players, croupier):    # Наступление случая, когда у всех "пасс". Открываем карты

    croupier.player_cards[0].ishidding = False
    print(f'Открываем карты! Набрано {croupier.get_value()} очков: {croupier.player_cards}\n')
    for i_player in players:
        if int(f'{i_player.get_value()}') > int(f'{croupier.get_value()}') \
                and i_player.get_value() <= 21:
            i_player.chip_balance += i_player.bet * 1.5
            print(f'{i_player.name}, у вас {i_player.get_value()} очков! '
                  f'Вы победили! Ваш баланс: {i_player.chip_balance}\n')
        elif int(f'{i_player.get_value()}') == int(f'{croupier.get_value()}'):
            i_player.chip_balance += i_player.bet
            print(f'{i_player.name}, у вас {i_player.get_value()} очков, ничья. '
                  f'Ваш баланс: {i_player.chip_balance}\n')
        else:
            print(f'{i_player.name}, у вас {i_player.get_value()} очков, '
                  f'Вы проиграли! Ваш баланс: {i_player.chip_balance}\n')


def play(player, card):  # Игровые действия во время одного цикла

    if player.name == 'Croupier':
        if player.get_value() < 17:
            player.hit(card)
            print(f'Карты крупье: {player.player_cards}\n')
        else:
            player.stand()
            player.check_bankrupt()
    else:
        if player.chip_balance + player.bet >= player.bet:
            if player.play_status is False:
                choice = input(f'{player.name} - набрано {player.get_value()} очков. '
                               f'Ваш выбор? 1 - взять карту, 2 - пас! ')
                if choice == '1':
                    player.hit(card)
                    print(f'{player.player_cards} набрано {player.get_value()} очков\n')
                    if player.get_value() > 21:
                        print(f'{player.name} - перебор! Вы проиграли!\n')
                        player.play_status = True
                elif choice == '2':
                    player.stand()
                else:
                    print('Не понял вас. Отвечайте только "1" или "2"')
                    play(player, card)
            else:
                pass
        else:
            print(f'{player.name} у Вас недостаточно средств!')


def start_game(players, deck, croupier):  # Начало игрового цикла. Сдаем по две карты  и проверяем на блэкджек

    new_deck = CardsDeck()
    for i_player in players:
        print(f'{i_player.name}: '
              f'баланс: {i_player.chip_balance}, '
              f'текущая ставка: {i_player.bet}')
    if len(deck.cards) <= len(players) * 5 or len(deck.cards) <= 10:
        deck.cards.extend(new_deck.cards)
    print('\nНачнем!\nТасуем колоду.\n')
    deck.shuffle()
    first_card = Card(deck.deal_card().rank, deck.deal_card().suit)
    first_card.ishidding = True
    croupier.add_card(first_card)
    croupier.add_card(deck.deal_card())
    print(f'Карты крупье: {croupier.player_cards}\n')
    print('Сдаем карты.\n')
    for i_player in players:
        i_player.player_cards = []
        i_player.add_card(deck.deal_card())
        i_player.add_card(deck.deal_card())
        print(f'Карты {i_player.name} - {i_player.player_cards} '
              f'набрано {i_player.get_value()} очков\n')
        if i_player.check_bj() and croupier.get_value() < 21:
            all([i_player.play_status for i_player in players])
            i_player.chip_balance += i_player.bet * 1.5
            print(f'{i_player.name}! Поздравляю! У вас Блэкджек!!! '
                  f'Ваш баланс: {i_player.chip_balance}\n '
                  f'Остальные игроки проиграли!\n')
            break
        else:
            pass
    if croupier.check_bj():
        croupier.player_cards[0].ishidding = False
        print(f'Открываем карты! Набрано {croupier.get_value()} очков: '
              f'{croupier.player_cards}\n')
        for i_player in players:
            i_player.play_status = True
            if i_player.get_value() != 21:
                print(f'BlackJack! {i_player.name}, Вы проиграли! Ваш баланс: {i_player.chip_balance}\n')
            else:
                i_player.chip_balance += i_player.bet
                print(f'{i_player.name}, у вас {i_player.get_value()} очков, ничья. '
                      f'Ваш баланс: {i_player.chip_balance}\n')
        all([i_player.play_status for i_player in players])
    while not all([i_player.play_status for i_player in players]):
        get_winner(players, deck, croupier)
    else:
        new_play(players, deck, croupier)


def get_winner(players, deck, croupier):  # Проверка на наступление победного сочетания

    for i_player in players:
        play(i_player, card=deck.deal_card())
    play(croupier, card=deck.deal_card())
    if croupier.isbankrupt:
        croupier_bankrupt(players, croupier)
    elif all([i_player.play_status for i_player in players]) and croupier.play_status:
        all_pass(players, croupier)
    else:
        get_winner(players, deck, croupier)


players_, deck_, croupier_ = get_players()
start_game(players_, deck_, croupier_)
# Было трудно!
