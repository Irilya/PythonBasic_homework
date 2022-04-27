

def slicer(num_tuple, num):


    if num_tuple.count(num) == 0:
        new_slicer = ()
    elif num_tuple.count(num) == 1:
        first_index = num_tuple.index(num)
        new_slicer = num_tuple[first_index:]
    else:
        first_index = num_tuple.index(num)
        short_list = num_tuple[first_index + 1:]
        second_index = short_list.index(num)
        second_index = second_index + first_index + 2
        new_slicer = num_tuple[first_index: second_index]

    return new_slicer


