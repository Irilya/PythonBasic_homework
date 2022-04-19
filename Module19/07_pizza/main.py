number_of_orders = int(input('Введите количество заказов: '))
count = 1
order_info = {}
while number_of_orders > 0:
    pizza_order = input(f'{count} заказ: ')
    pizza_order = pizza_order.split()
    if pizza_order[0] in order_info.keys():
        if pizza_order[1] in order_info[pizza_order[0]].keys():
            order_info[pizza_order[0]][pizza_order[1]] += int(pizza_order[2])
        else:
            order_info[pizza_order[0]][pizza_order[1]] = int(pizza_order[2])
    else:
        order_info[pizza_order[0]] = {pizza_order[1]: int(pizza_order[2])}
    number_of_orders -= 1
    count += 1


for i_name in order_info.values():
    list_i_name = list(i_name.items())
    list_i_name.sort(key=lambda i: i[1])
    list_i_name = dict(list_i_name)
    for name in order_info:
        if order_info[name] == i_name:
            order_info[name] = list_i_name
            break



for i_name in order_info:
    print(f'\n{i_name}: ')
    for j_name in order_info[i_name]:
        print(f'\n{j_name}: {order_info[i_name][j_name]}')



