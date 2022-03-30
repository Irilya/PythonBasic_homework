original_text = input('Введите текст: ')

volves = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
volves_in_text = [letter for letter in original_text if letter in volves]
print('Список гласных букв: ', volves_in_text)
print('Длина списка: ', len(volves_in_text))



