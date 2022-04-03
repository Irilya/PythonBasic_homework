original_text = input('Введите строку: ')

new_text = ''
count = 1
for i in range(0, len(original_text) - 1):
    if original_text[i] == original_text[i + 1]:
        count += 1
    else:
        new_text = f'{new_text}{original_text[i]}{str(count)}'
        count = 1

print(f'Закодированная строка: {new_text}{original_text[i]}{str(count)}')