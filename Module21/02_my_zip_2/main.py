

def z_func(*args):

    len_min = [len(i_list) for i_list in args]
    all_dic = {i_sec: list(i_list) for i_sec, i_list in enumerate(args)}
    len_min = sorted(len_min)

    res_list = [tuple([i_vol[i_num] for i_vol in all_dic.values()])
                for i_num in range(len_min[0])]

    return res_list


# list_1 = [1, 2, 3, 4]
# list_2 = ('a', 'b', 'c')
# list_3 = {'ab': 1, 'cd': 1, 'ef': 1}
# list_res = z_func(list_1, list_2, list_3)
#
# print(list_res)
