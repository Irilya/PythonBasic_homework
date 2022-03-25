
import random

first_command = [round(random.uniform(5.0, 10.0), 2) for x in range(20)]
second_command = [round(random.uniform(5.0, 10.0), 2) for y in range(20)]
winner_list = [(first_command[i] if first_command[i] > second_command[i]
                else second_command[i])
                for i in range(20)]


print('Первая команда: ', first_command)
print('Вторая команда: ', second_command)
print('Победители тура: ', winner_list)

