

def voice_calculator(file):

    operation = ['+', '-', '*', '/', '%', '//', '**']
    total_summ = 0
    with open(file, 'r') as calculator:
        for i_line in calculator:
            i_line = i_line.split()
            try:
                if len(i_line) != 3:
                    raise IndexError
                elif not i_line[0].isdecimal() and not i_line[2].isdecimal():
                    raise BaseException
                elif i_line[1] not in operation:
                    raise ValueError
            except (IndexError, ValueError, BaseException):
                answer = (input(f'В строке {" ".join(i_line)} обнаружена ошибка, хотите исправить? Да/Нет: '))
                if answer.lower() == 'да':
                    i_line = input('Введите исправленную строку: ')
                    res = eval(i_line)
                    print(res)
                    total_summ += res
            else:
                try:
                    res = eval(' '.join(i_line))
                    print(res)
                    total_summ += res
                except (ZeroDivisionError, BaseException):
                    answer = (input(f'В строке {" ".join(i_line)} обнаружена ошибка, хотите исправить? Да/Нет: '))
                    if answer.lower() == 'да':
                        i_line = input('Введите исправленную строку: ')
                        res = eval(i_line)
                        print(res)
                        total_summ += res

    print(total_summ)


voice_calculator('calc.txt')


