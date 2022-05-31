import os


def original_txt_file_save(text, work_path, name):

    original_work_path = ''
    work_path = work_path.split()
    for elem in work_path:
        original_work_path = os.path.abspath(os.path.join(os.path.sep, original_work_path, elem))
    original_work_path = os.path.abspath(os.path.join(os.path.sep, original_work_path, name))

    if not os.path.exists(original_work_path):
        my_text = open(original_work_path, 'w', encoding='utf-8')
        my_text.write(str(text))
        print('\nФайл успешно сохранён!')
        my_text.close()
        my_text = open(original_work_path, 'r', encoding='utf-8')
        print('Содержимое файла: ')
        print(my_text.read())
        my_text.close()
    else:
        choice = input('Вы действительно хотите перезаписать файл? (y/n)')
        if choice == 'y':
            my_text = open(original_work_path, 'w', encoding='utf-8')
            my_text.write(str(text))
            print('Файл успешно перезаписан!')
            my_text.close()
            my_text = open(original_work_path, 'r', encoding='utf-8')
            print('Содержимое файла: ')
            print(my_text.read())
            my_text.close()
        else:
            print('Хорошо! Не перезаписывем.')


original_text = input('Введите строку: ')

path_dir = input('Куда хотите сохранить документ? '
                 'Введите последовательность папок (через пробел): ')
orig_file_name = input('Введите имя файла: ')

original_txt_file_save(original_text, path_dir, orig_file_name)
