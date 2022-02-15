

def number_min_devisor():


    number_N = int(input('Введите число: '))
    if number_N > 1:
        for number in range(2, number_N + 1):
            if number_N % number == 0:
                print('Наименьший делитель, отличный от единицы: ', number)
                break


number_min_devisor()