from typing import List


prime_list: List[int] = list(filter(lambda elem: elem > 1 and not any(elem % item == 0
                                    for item in range(2, round(elem ** (1/2)) + 1)), range(1001)))

print(prime_list)


def prime_filter():
    for elem in range(2, 1001):
        for item in range(2, round(elem ** (1/2)) + 1):
            if elem % item == 0:
                break
        else:
            print(elem)


prime_filter()
