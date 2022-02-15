

def operations_with_numbers():


    number_N = int(input('Введите число: '))

    count_digit_N = 0
    summ_digit_N = 0
    while number_N > 0:
        digit_N = number_N % 10
        summ_digit_N += digit_N
        count_digit_N += 1
        number_N //= 10

    print('Сумма цифр в числе: ', summ_digit_N)
    print('Количество цифр в числе: ', count_digit_N)
    print('Разность суммы цифр и их количества: ', summ_digit_N - count_digit_N)

operations_with_numbers()

