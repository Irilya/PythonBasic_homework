

def get_unhappy_years():


    first_year = int(input('Введите первый год: '))
    second_year = int(input('Введите второй год: '))
    count = 1
    first_digit_in_year = 1
    second_digit_in_year  = 0
    for item in range(first_year, second_year + 1):
        first_digit_in_year = item // 1000
        second_digit_in_year = (item // 100) % 10
        if first_digit_in_year != second_digit_in_year:
            if (item // 10) % 10 == first_digit_in_year or (item // 10) % 10 == second_digit_in_year:
                count += 1
                if item % 10 == (item // 10) % 10:
                    count += 1
            if count == 3:
                print(item)
            count = 1
        elif first_digit_in_year == second_digit_in_year:
            count = 2
            if item % 10 == first_digit_in_year and (item // 10) % 10 != first_digit_in_year:
                count += 1
            elif (item // 10) % 10 == first_digit_in_year and item % 10 != first_digit_in_year:
                count += 1
        if count == 3:
            print(item)


get_unhappy_years()


