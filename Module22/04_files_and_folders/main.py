import os


def file_directory_count(work_path):

    count_dir = 0
    count_file = 0
    file_size = 0
    for i_elem in os.listdir(work_path):
        path = os.path.join(work_path, i_elem)
        if os.path.isfile(path):
            file_size += os.path.getsize(path)/1024
            count_file += 1
            count_dir += 0
        elif os.path.isdir(path):

            d_count, count, size = file_directory_count(path)
            count_file += count
            count_dir += d_count + 1
            file_size += size

    return count_dir, count_file, file_size


abs_path = os.path.abspath(os.path.join(os.path.sep, 'SkillBox'))
dir_count, file_count, size_files = file_directory_count(abs_path)
print(f'\n{abs_path}')
print(
    f'\nРазмер каталога (в Кб): {size_files}'
    f'\nКоличество подкаталогов: {dir_count}'
    f'\nКоличество файлов: {file_count}'
    )
