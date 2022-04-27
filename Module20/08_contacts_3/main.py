

def change_phone_dict():

    phone_dict = {}
    while True:
        action = int(input('Введите номер действия '
                           '\n1. Добавить контакт'
                           '\n2. Найти человека : ')
                     )
        if action == 1:
            new_contact = input('Введите имя и фамилию нового контакта (через пробел): ')
            new_contact = tuple(new_contact.split())
            contact_phone = int(input('Введите номер телефона: '))
            phone_dict[new_contact] = contact_phone
            print(f'Текущий словарь контактов: \n{phone_dict}')
        elif action == 2:
            name = input('Введите фамилию для поиска: ')
            for i_name, i_phone in phone_dict.items():
                if name in i_name:
                    print(i_name[0], i_name[1], i_phone)
        else:
            break


change_phone_dict()
