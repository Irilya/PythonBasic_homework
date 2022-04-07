import re


original_text = input('Сообщение: ')
pattern = re.compile(r'(\W+)')
new_text = pattern.split(original_text)

new_text_code = ''
for item in new_text:
    if item.isalpha():
        new_text_code += item[::-1]
    else:
        new_text_code += item

print(f'Новое сообщение: {new_text_code}')





