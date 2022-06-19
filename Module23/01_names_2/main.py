line_count = 0
symbol_summ = 0

try:
    with open('people.txt', 'r') as people_list:
        for i_line in people_list:
            line_count += 1
            try:
                line_length = len(i_line)
                if i_line.endswith('\n'):
                    line_length -= 1
                if line_length <= 3:
                    raise ValueError
            except ValueError:
                print(f'Длина cтроки номер {line_count} менее 3х символов.')
                with open('log.txt', 'a') as log_info:
                    log_info.write(f'ValueError - Длина cтроки номер {line_count} менее 3х символов.')
            symbol_summ += line_length

except FileNotFoundError:
    print(f'Такого файла не существует.')
    with open('log.txt', 'w') as log_info:
        log_info.write(f'FileNotFoundError - Такого файла не существует.')
finally:
    print(f'Найденная сумма символов {symbol_summ}')
