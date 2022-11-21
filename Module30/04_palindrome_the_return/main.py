import collections
from typing import Any


def can_be_poly(my_string: str) -> Any:
    deq_string = collections.deque(my_string)
    while len(deq_string) > 1:
        if deq_string[0] == deq_string[-1]:
            deq_string.pop()
            deq_string.popleft()
        else:
            return False
        return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
