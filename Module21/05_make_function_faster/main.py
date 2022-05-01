# def calculating_math_func(data=5):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     # result /= data ** 3
#     # result = result ** 10
#     return result


def calculating_math_func(data, factorial_dic={}):

    list_keys = sorted(factorial_dic.keys())
    if factorial_dic != {} and data >= list_keys[0]:
        for key in list_keys:
            if data >= key:
                index = key
                fact = factorial_dic[key]
                break
    else:
        fact = 1
        index = 0

    for ind in range(index + 1, data + 1):
        fact *= ind
    factorial_dic[data] = fact
    result = fact
    result /= data ** 3
    result = result ** 10

    return result
