players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}


players_list = [(i_name + i_vol) for i_name, i_vol in players.items()]

print(f'Результат работы программы: \n{players_list}')
