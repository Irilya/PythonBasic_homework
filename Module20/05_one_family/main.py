family_dict = {
    ("Петрова", "Нина"): 72,
    ("Иванов", "Евгений"): 32,
    ("Петров", "Павел"): 28,
    ("Сидоров", "Никита"): 35,
    ("Сидоров", "Павел"): 10,
    ("Сидорова", "Алина"): 34,
    ("Городницкая", "Елена"): 42,
    ("Кардаш", ""): 35,
    ("Городницкий", "Александр"): 15,
    ("Петровский", "Леонид"): 18
}



family_surname = input('Введите фамилию: ')
family_surname = family_surname.lower()
for i_person in family_dict:
    if family_surname[0:len(family_surname)-2] in i_person[0].lower()[0:]:
        if abs(len(family_surname) - len(i_person[0])) <= 2:
            print(i_person[0], i_person[1], family_dict[i_person])


