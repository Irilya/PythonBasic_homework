

def check_registration_info(file):

    count_line = 0
    with open(file, 'r', encoding='utf-8') as check_info:
        for i_line in check_info:
            try:
                count_line += 1
                line = i_line.split()
                if len(line) != 3:
                    raise IndexError
                elif not line[0].isalpha():
                    raise NameError
                elif '@' not in line[1] or '.' not in line[1]:
                    raise SyntaxError
                elif int(line[2]) not in range(10, 100):
                    raise ValueError
            except ValueError:
                with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
                    bad_file.write(
                            f'\nВ строке {count_line}: {" ".join(line)} '
                            f'Поле «Возраст» НЕ является числом от 10 до 99'
                            )
            except SyntaxError:
                with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
                    bad_file.write(
                        f'\nВ строке {count_line}: {" ".join(line)} '
                        f'Поле «Имейл» НЕ содержит @ и . (точку)'
                        )
            except NameError:
                with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
                    bad_file.write(
                        f'\nВ строке {count_line}: {" ".join(line)} '
                        f'Поле имени содержит НЕ только буквы.'
                        )
            except IndexError:
                with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
                    bad_file.write(
                        f'\nВ строке {count_line}: {" ".join(line)} '
                        f'НЕ присутствуют все три поля.'
                        )
            else:
                with open('registrations_good.log', 'a', encoding='utf-8') as good_file:
                    good_file.write(f"\n{' '.join(line)}")


check_registration_info('registrations.txt')
