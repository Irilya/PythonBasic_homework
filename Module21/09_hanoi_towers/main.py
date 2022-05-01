

def hanoi_towers(num, start, finish):

    if num == 1:
        print(f'Переложить диск {num} со стержня номер {start} на стержень номер {finish}')
    else:
        additional = 6 - start - finish
        hanoi_towers(num - 1, start, additional)
        print(f'Переложить диск {num} со стержня номер {start} на стержень номер {finish}')
        hanoi_towers(num - 1, additional, finish)


discs = int(input('Введите количество дисков: '))
hanoi_towers(discs, 1, 3)
