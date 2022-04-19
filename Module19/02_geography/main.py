countries_num = int(input('Количество стран: '))
countries_city = {}
count = 1


while countries_num > 0:
    country = input(f'{count}-я страна: ')
    country = country.split()
    countries_city[country[0]] = [city for city in country[1:]]
    count += 1
    countries_num -= 1


city_count = 1
while city_count <= 3:
    city = input(f'\n{city_count} город: ')
    for country in countries_city:
        if city in countries_city[country]:
            print(f'Город {city} расположен в стране {country}.')
            break
    else:
        print(f'По городу {city} данных нет.')
    city_count += 1


