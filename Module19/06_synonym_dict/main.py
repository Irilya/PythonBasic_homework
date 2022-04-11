num_words = int(input('Введите количество пар слов: '))

sinonim_dict = {}
count = 1
while num_words > 0:
    sinonim_word = input(f'{count}-я пара (через пробел): ')
    sinonim_word = sinonim_word.lower().split()
    sinonim_dict[sinonim_word[0]] = sinonim_word[1]
    sinonim_dict[sinonim_word[1]] = sinonim_word[0]
    count += 1
    num_words -= 1


original_word = ''
print(f'\nДля завершения работы введите слово конец.\n')
while original_word != 'конец':
    original_word = input('\nВведите слово: ').lower()
    for i_word in sinonim_dict.keys():
        if i_word == original_word:
            print(f'Синоним: {sinonim_dict[i_word]}')
            break
    else:
        print('Такого слова в словаре нет.')




