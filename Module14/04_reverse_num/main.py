

def get_opossite_number_whole_part(whole_number_N):


    opposite_number = ''
    while whole_number_N > 0:
        digit_number = whole_number_N % 10
        opposite_number += str(digit_number)
        whole_number_N = whole_number_N // 10
    opposite_number = int(opposite_number)

    return int(opposite_number)


def get_opossite_number_fract_part(fract_number_N):


    count = 0
    while fract_number_N % 1 > 0:
        fract_number_N *= 10
        count += 1
    opossite_number_fract_part = get_opossite_number_whole_part(int(fract_number_N))
    opossite_number_fract_part = opossite_number_fract_part * 10 ** (-count)

    return opossite_number_fract_part


def summ_two_opposite_numbers():


    number_X = float(input('Введите первое число: '))
    number_Y = float(input('Введите второе число: '))
    count = 1
    two_opposite_numbers = 0
    number_N = number_X
    while count < 3:
        whole_number_N = int(number_N)
        fract_number_N = round((number_N - whole_number_N), 2)
        number_N = get_opossite_number_whole_part(whole_number_N) + get_opossite_number_fract_part(fract_number_N)
        print('число ', count, 'наоборот: ', number_N)
        two_opposite_numbers += number_N
        count += 1
        number_N = number_Y

    print('Сумма чисел: ', two_opposite_numbers)

summ_two_opposite_numbers()








