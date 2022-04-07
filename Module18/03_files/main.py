fail_name = input('Название файла: ')

symbols_err = ' '.join('@№$%^&*()')
symbols_err = symbols_err.split()
symbols_err = tuple(symbols_err)

if fail_name.startswith(symbols_err):
    print('Ошибка: название начинается на один из специальных символов')
elif not fail_name.endswith('.txt' or '.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')


