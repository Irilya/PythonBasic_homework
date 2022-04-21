

def secret_competitions():

    count = 1
    play_data_dic = {}
    print('Записи (результат и имя): ')

    while count <= n:
        play_data = input(f'{count}-я запись: ')
        play_data_dic[count] = play_data.split()
        count += 1

    person = []
    for i_person in play_data_dic.values():
        if i_person[1] not in person:
            person.append(i_person[1])

    return play_data_dic, len(person)


def competitions_results(play_dictionary):

    dictionary_sorted = {
        i_num: i_res for i_num, i_res
        in sorted(play_dictionary.items(), key=lambda i_num: int(i_num[1][0]), reverse=True)
    }

    print('\nИтоги соревнований: \n')
    table_best = {}

    for i_num, i_name in dictionary_sorted.values():
        if len(table_best) < 3 and i_name not in table_best.keys():
            table_best[i_name] = i_num

    return table_best


n = int(input('Сколько записей вносится в протокол? '))

while n < 3:
    print('Недостаточное число участников')

    break

else:
    play_dictionary, person = secret_competitions()
    while int(person) < 3:
        print('Недостаточное число участников.')

        break

    else:
        result_dict = competitions_results(play_dictionary)
        for num, res in enumerate(result_dict):
            print(f'{num + 1}-е место. {res} {result_dict[res]}')
