
import random

number_N = int(input('Количество чисел в списке: '))
list = [random.randint(0, 2) for x in range(number_N)]
original_list = list[:]
if original_list.count(0) > 0:
    fl = original_list.index(0)

    for i in range(number_N):
        if original_list[i] != 0 and i < fl:
            original_list[i] = original_list[i]
        elif original_list[i] != 0 and i > fl:
            original_list[fl], original_list[i] = original_list[i], original_list[fl]
            fl = original_list.index(0)
    original_list_after = original_list[0: fl]

print('Список до сжатия: ', list)
print('Список после сжатия: ', original_list_after)



# Если стоит задача просто убрать нули, то все гораздо проще.

# number_N = int(input('Количество чисел в списке: '))
# list = [random.randint(0, 2) for x in range(number_N)]
# original_list_after = [x for x in list if x != 0]
# print('Список до сжатия: ', list)
# print('Список после сжатия: ', original_list_after)



