import random


original_list = [random.randint(0, 100) for x in range(10)]
new_list = [(original_list[i], original_list[i + 1]) for i in range(0, 9, 2)]

print(original_list)
print(new_list)

list_1 = []
list_2 = []
for i, j in enumerate(original_list):
    if i % 2 == 0:
        list_1.append(j)
    else:
        list_2.append(j)

new_list = []
for k, n in tuple(zip(list_1, list_2)):
    new_list.append((k, n))

print(new_list)
