alf_list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
            'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

original_text = input('Введите сообщение: ')
original_text_code = [letter for letter in original_text]
code_shift = int(input('Введите сдвиг: '))


def text_codding(text):


    for i in range(len(original_text_code)):
        if original_text_code[i] in alf_list:
            j = alf_list.index(original_text_code[i])
            original_text_code[i] = alf_list[(j + code_shift) % 33]



text_codding(original_text)


print('Зашифрованное сообщение: ', ''.join(original_text_code))




