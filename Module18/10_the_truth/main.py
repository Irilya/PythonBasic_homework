alf_list = 'abcdefghijklmnopqrstuvwxyz'
alf_list_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

original_text = input('text: ')

shift_code = 0

for word in original_text.split():
    while shift_code == 0:
        for letter in word:
            if letter in alf_list_up:
                    shift_code = len(word) - word.index(letter)
    else:
        break


original_text_new = ''

for word in original_text.split():
    new_word = ''
    for i in range(len(word)):
        new_word += word[i - shift_code % len(word)]
    if new_word.endswith('/'):
            shift_code += 1

    original_text_new += new_word + ' '

original_text_new = original_text_new.replace('/', '\n')
original_text_new = original_text_new.replace('(', "'")
original_text_new = original_text_new.replace('.', '-')



for shift in range(1, 26):
    print(f'\nсдвиг равен: {shift}')


def text_with_shift(text, shift):


    translated_text = ''
    for i in range(len(text)):
        if text[i] in alf_list:
            j = alf_list.index(text[i])
            letter = alf_list[(j + shift) % 26]
            translated_text += letter
        elif text[i] in alf_list_up:
            j = alf_list_up.index(text[i])
            letter = alf_list_up[(j + shift) % 26]
            translated_text += letter
        else:
            translated_text += text[i]

    return translated_text

for shift in range(1, 26):
    print(f'\nсдвиг равен: {shift}')
    print(text_with_shift(original_text_new, shift))





