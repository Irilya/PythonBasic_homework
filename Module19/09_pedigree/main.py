number_N = int(input('Введите количество человек: '))

parent_tree = {}
count = 1
branch_num = 0
while number_N - 1 > 0:
    child_parent = input(f'{count}-я пара: ')
    child_parent = child_parent.split()
    count += 1
    number_N -= 1

    if parent_tree == {}:
        parent_tree[child_parent[1]] = branch_num
        branch_num += 1
        parent_tree[child_parent[0]] = branch_num

    if parent_tree[child_parent[1]] == branch_num - 1:
        parent_tree[child_parent[0]] = branch_num

    else:
        branch_num += 1
        parent_tree[child_parent[0]] = branch_num

print(f'\nВысота» каждого члена семьи:\n')
for name in sorted(parent_tree.keys()):
    print(f'{name} : {parent_tree[name]}')
