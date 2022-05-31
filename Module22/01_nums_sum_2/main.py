

def get_sum_digits(file):
    
    origin_file = open(file, 'r')
    summ_dig = 0
    for i_str in origin_file:
        for elem in i_str:
            if elem.isdigit():
                summ_dig += int(elem)

    answer = open('answer.txt', 'w')
    answer.write(str(summ_dig))
    answer.close()
    origin_file.close()


get_sum_digits('numbers.txt')

original_file = open('numbers.txt', 'r')
answer_sum = open('answer.txt', 'r')
print(f'\nСодержимое файла numbers.txt: \n{original_file.read()}')
print(f'\nСумма чисел в файле: \n{answer_sum.read()}')
answer_sum.close()
original_file.close()
