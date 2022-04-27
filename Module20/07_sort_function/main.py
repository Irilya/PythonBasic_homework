# original_tuple = (6, 3, -1, 8, 4, 10, -5)

def sort_tuple(original_tuple):

    new_tuple = tuple()
    for i_num in original_tuple:
        if type(i_num) is not int:
            new_tuple = original_tuple

            break

        else:
            original_list = list(original_tuple)
            original_list = sorted(original_list)
            new_tuple = tuple(original_list)

    return new_tuple

# print(sort_tuple(original_tuple))
