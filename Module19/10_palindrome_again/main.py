original_text = input('Введите строку: ')
count = 0


def get_original_dict(text):


    original_dict = {}
    for letter in original_text:
        if letter in original_dict:
            original_dict[letter] += 1
        else:
            original_dict[letter] = 1
    return original_dict


for letter in get_original_dict(original_text):
    if count <= 1:
        if get_original_dict(original_text)[letter] % 2 != 0:
            count += 1
    else:
        print('Нельзя сделать палиндромом')
        break

if count <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')


