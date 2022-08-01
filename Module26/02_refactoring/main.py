list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

my_list = ((x, y) for x in list_1 for y in list_2)
for x, y in my_list:
    result = x * y
    print(x, y, result)
    if result == to_find:
        print('Found!!!')
        break
