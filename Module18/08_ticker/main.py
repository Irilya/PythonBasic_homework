first_text = input('Первая строка: ')
second_text = input('Вторая строка: ')
shift = second_text.index(first_text[0])
check_str = ''
for i in range(len(second_text)):
    j = (i + shift) % len(second_text)
    check_str += second_text[j]
if first_text == check_str:
    print(f'Первая строка получается из второй со сдвигом {shift}.')
else:
    print(f'Первую строку нельзя получить из второй с помощью '
          f'циклического сдвига.'
          )



