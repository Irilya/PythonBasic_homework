import os
import re


def count_sign(file):

    letters_min = {}
    count_str = 0
    count_words = 0
    count_letters = 0
    original = open(file, 'r')
    for i_str in original:
        count_str += 1
        i_str = i_str.lower().expandtabs().rstrip()
        j_str = re.split(" -- | ", i_str)
        count_words += len(j_str)
        for sign in i_str:
            if sign.isalpha():
                count_letters += 1
                if sign not in letters_min:
                    letters_min[sign] = 1
                else:
                    letters_min[sign] = letters_min[sign] + 1

    original.close()
    return count_str, count_words, count_letters, letters_min


def letter_min_count(dictinory):

    min_result = ''
    val_min = sorted(dictinory.values())
    val_min = val_min[0]
    for key, value in dictinory.items():
        if value == val_min:
            min_result = key
            if min_result:
                break

    return min_result, val_min


file_path = os.path.join('..', '02_zen_of_python', 'zen.txt')
str_count, words_count, letters_count, min_letters = count_sign(file_path)
result_min, min_count = letter_min_count(min_letters)
print(
    f'Количество строк в файле: {str_count}'
    f'\nКоличество слов в файле: {words_count}'
    f'\nКоличество букв в файле: {letters_count}'
    f'\nБуква {result_min} встречается наименьшее количество раз - {min_count}'
    )
