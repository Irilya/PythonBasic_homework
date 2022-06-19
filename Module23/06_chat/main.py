import datetime


def my_test_chat(name):

    while True:
        answer = input(f'Хотите просмотреть чат или отправить сообщение?'
                       f' (1 - просмотреть чат, '
                       f' 2 - отправить сообщение'
                       f' 3 - выход из чата) ')
        if answer == '1':
            try:
                with open('chat_info.txt', 'r', encoding='utf-8') as chat:
                    print(chat.read())
            except FileNotFoundError:
                print(f'Упс! Никто ничего не написал!')
                answer = input(f'{name}, хотите написать сообщение? да/нет')
                if answer.lower() == 'да':
                    message = input(f'Введите текст сообщения: ')
                    with open('chat_info.txt', 'a', encoding='utf-8') as chat:
                        chat.write(f"\n{datetime.datetime.now()} {name}: {message}")
                elif answer.lower() == 'нет':
                    print(f'Пока! Ждем тебя снова, {name}')
                    start_chat()
        elif answer == '2':
            message = input(f'Введите текст сообщения: ')
            with open('chat_info.txt', 'a', encoding='utf-8') as chat:
                chat.write(f"\n{datetime.datetime.now()} {name}: {message}")
        elif answer == '3':
            print(f'Пока! Ждем тебя снова, {name}')
            start_chat()
        else:
            print('Непонятная команда...')


def start_chat():

    name_list = []
    username = input('Давайте знакомиться. Как Вас зовут? ')
    if username not in name_list:
        name_list.append(username)
        print(f'Добро пожаловать, {username}!')
        my_test_chat(username)
    else:
        username = input('Такое имя уже есть в чате. Назовитесь иначе, чтобы вас не перепутали.)))')
        name_list.append(username)
        print(f'Добро пожаловать, {username}!')
        my_test_chat(username)


start_chat()


