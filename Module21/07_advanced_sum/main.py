

def calculator(*args):

    global total_sum
    for num in args:
        if isinstance(num, int):
            total_sum += num
        else:
            for i in range(len(num)):
                if isinstance(num[i], int):
                    total_sum += num[i]
                else:
                    calculator(num[i])

    return total_sum


total_sum = 0
list_n = [[1, 2, [3]], [1], 3]
print(calculator(list_n))
