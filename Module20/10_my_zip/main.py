

def z_func(list_1, list_2):

    lenth = sorted([len(list_1), len(list_2)])

    dic_1 = [i_vol for i_num, i_vol in enumerate(list_1)]
    dic_2 = [i_vol for i_num, i_vol in enumerate(list_2)]

    for i_num in range(lenth[0]):

        yield dic_1[i_num], dic_2[i_num]


list_1 = 'abcd'
list_2 = (10, 20, 30, 40)

list_new = z_func(list_1, list_2)
print(list_new)
for i in list_new:
    print(i)
