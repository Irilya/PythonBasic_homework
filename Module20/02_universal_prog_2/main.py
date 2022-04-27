

def is_prime(num):

    check = 0
    for i_num in range(2, num // 2 + 1):
        if num % i_num == 0:
            check += 1
            break
    if check == 0 and num > 1:
        return True
    else:
        return False


def crypto_prime_index(object):

    return [i_val for i_index, i_val in enumerate(object) if is_prime(i_index)]
