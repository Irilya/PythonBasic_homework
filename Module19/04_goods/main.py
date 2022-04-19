goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

print(f'Результат работы программы: ')


for key_good in goods.keys():
    price_values = store.get(goods.get(key_good, {}))
    total_quantity = 0
    total_price = 0
    for j_key in price_values:
        quantity_value = j_key['quantity']
        total_quantity += int(quantity_value)
        price_value = j_key['price']
        total_price += quantity_value * price_value
    print(f'\n{key_good} - {total_quantity} штук, стоимость {total_price} рубля')


