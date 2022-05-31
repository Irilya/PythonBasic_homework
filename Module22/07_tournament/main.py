

def get_result_after_first_tour(file):

    info_first_tour = open(file, 'r')
    ball_min = 0
    count = 0
    second_tour = []
    for line in info_first_tour:
        ball = int(line[-3:])
        if count == 0:
            ball_min = ball
            count += 1
        else:
            if ball > ball_min:
                ball = 1000 - ball
                second_tour.append(str(ball) + ' ' + line)

    second_tour = sorted(second_tour)
    info_first_tour.close()

    return second_tour


def format_second_tour_list(ball_list):

    second_list = open('second_tour.txt', 'w')
    second_tour_list = []
    count_list = 0
    for elem in ball_list:
        count_list += 1
        elem = elem.split()
        second_tour_list.append(f'{count_list}) {elem[2][0]}. {elem[1]} {elem[3]}\n')
    second_tour_list.insert(0, f'{count_list}\n')
    second_tour_list = ''.join(second_tour_list)
    second_list.write(second_tour_list)
    second_list.close()
    second_tour_table = open('second_tour.txt', 'r')
    print(second_tour_table.read())
    second_tour_table.close()


list_tour = get_result_after_first_tour('first_tour.txt')
format_second_tour_list(list_tour)
