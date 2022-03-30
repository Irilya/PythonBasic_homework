number_N = int(input('Введите длину списка: '))

generated_list = [(1 if x % 2 == 0 else x % 5) for x in range(10)]
print('Результат: ', generated_list)

