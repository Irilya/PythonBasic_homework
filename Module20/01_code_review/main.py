students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)



def get_interests(dictionary):


    if len(dictionary) > 0:
        total_list_interests = []
        total_len = 0
        pairs = []

        for i_num, j_num in dictionary.items():
            total_list_interests += j_num['interests']
            total_len += len(j_num['surname'])
            pairs.append((i_num, j_num['age']))

        return pairs, total_list_interests, total_len
    else:
        print('Словарь пуст')


dictionary = students
pairs, total_list_interests, total_len = get_interests(dictionary)

print(f'"ID студента — возраст": {pairs}')
print(f'Полный список интересов всех студентов: {total_list_interests}')
print(f'Общая длина всех фамилий студентов: {total_len}')



