

def fibo_num(num):

    if num in (1, 2):
        return 1
    return fibo_num(num - 1) + fibo_num(num - 2)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))

fibo = fibo_num(num_pos)
print(f'Число: {fibo}')
