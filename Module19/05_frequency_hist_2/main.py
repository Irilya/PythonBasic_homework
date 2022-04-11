original_text = input('Введите текст: ')


def get_original_dict(text):


    original_dict = {}
    for letter in original_text:
        if letter in original_dict:
            original_dict[letter] += 1
        else:
            original_dict[letter] = 1
    return original_dict


def get_invert_dict(text):


    invert_dic = {}
    original_dict = get_original_dict(text)
    for i_sym in original_dict:
        if original_dict[i_sym] in invert_dic.keys():
            invert_dic[original_dict[i_sym]] += list(i_sym)
        else:
            invert_dic[original_dict[i_sym]] = list(i_sym)
    return invert_dic


print('\nОригинальный словарь частот:\n')
for i_sym in sorted(get_original_dict(original_text).keys()):
    print(i_sym, ':', get_original_dict(original_text)[i_sym])

print('\nИнвертированный словарь частот:\n')
for j_sym in sorted(get_invert_dict(original_text).keys()):
    print(j_sym, ':', get_invert_dict(original_text)[j_sym])


