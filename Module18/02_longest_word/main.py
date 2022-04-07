original_text = input('Введите строку: ')
original_text = original_text.split(' ')
word_max = 0
words_len = [len(word) for word in original_text]
for item in words_len:
    if item > word_max:
        word_max = item
ind = words_len.index(word_max)

print(f'Самое длинное слово: {original_text[ind]}')
print(f'Длина этого слова: {word_max}')




