class Student:

    def __init__(self, name, grup, progress):

        self.name = name
        self.grup = grup
        self.progress = progress

    def average_progress(self):

        progress_summ = 0
        if len(self.progress) == 5:
            for num in self.progress:
                progress_summ += num
            average = progress_summ / 5
            return average
        else:
            print('Неверное количество оценок')

    def info_student(self):

        info = [self.name, self.grup, self.progress]
        return info


def get_student_list(people_list):

    list_of_student = []
    for item in people_list:
        name = item[0]
        grup = item[1]
        progress = item[2]
        student = Student(name, grup, progress)
        average = student.average_progress()
        list_of_student.append([average, student.info_student()])

    list_of_student = sorted(list_of_student)
    return list_of_student


def print_info_student_list(people_list):

    for student in people_list:
        print('Фамилия/Имя - {}\t Группа - {}\t Оценки по предметам - {}\t Средний балл - {}'.format(
            student[1][0], student[1][1], student[1][2], student[0]
            )
        )


student_list = [
    ['Иванов Петр', 'G005', [4, 4, 5, 3, 5]],
    ['Пименов Василий', 'F013', [3, 4, 4, 3, 5]],
    ['Попов Алексей', 'F013', [5, 5, 5, 5, 5]],
    ['Северова Инна', 'G001', [4, 4, 5, 5, 5]],
    ['Мэр Виктортия', 'G001', [3, 4, 4, 4, 5]],
    ['Гатилова Ирина', 'F013', [5, 5, 5, 5, 5]],
    ['Ветер Дмитрий', 'G005', [4, 4, 5, 4, 5]],
    ['Елисеев Виталий', 'F013', [5, 5, 5, 4, 5]],
    ['Иглов Александр', 'G005', [4, 3, 3, 3, 5]],
    ['Стеклова Екатерина', 'G001', [5, 5, 4, 4, 5]]
    ]

people_list = get_student_list(student_list)
print_info_student_list(people_list)
