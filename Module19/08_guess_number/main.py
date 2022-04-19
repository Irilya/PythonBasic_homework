number_max = int(input('Введите максимальное число: '))
solution = [str(number) for number in range(1, number_max + 1)]

while True:
    if len(solution) == 1:
        print('Артём загадал число: ', solution[0])
        break

    else:
        boris_numbers = input('Нужное число есть среди вот этих чисел? ')
        if boris_numbers == 'Помогите!':
            print('Артём мог загадать следующие числа: ')
            for num in solution:
                print(num, end=' ')
            break

        else:
            answer_a = input('Ответ Артёма: ')
            boris_numbers = boris_numbers.split()
            if answer_a == 'Нет':
                for item in boris_numbers:
                    if item in solution:
                        solution.remove(item)

            elif answer_a == 'Да':
                solution = boris_numbers


