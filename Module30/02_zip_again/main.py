from typing import List


letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

numbers_letters: List[tuple] = list(map(lambda let, num: (let, num), letters, numbers))
print(numbers_letters)
