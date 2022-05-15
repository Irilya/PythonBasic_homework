

def list_of_num(num_n):

    if num_n != 0:
        num_minus = list_of_num(num_n - 1)
    else:
        return 0
    print(num_n - num_minus)
    return num_minus


num = int(input('Введите число: '))
list_of_num(num)
