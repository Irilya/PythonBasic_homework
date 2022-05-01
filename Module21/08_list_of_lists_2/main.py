
def open_list(list_original):

    if not list_original:
        return []

    res = open_list(list_original[:-1]) + (
        [list_original[-1]] if not isinstance(list_original[-1], list)
        else open_list(list_original[-1])
    )
    return res


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(open_list(nice_list))
