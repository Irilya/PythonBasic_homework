

def letters_value(file):

    alfabeta = 'abcdefghijklmnopqrstuvwxyz'
    all_count = 0
    letters_dic = {}
    original_text = open(file, 'r')
    for line in original_text:
        line = line.lower()
        for sign in line:
            if sign in alfabeta:
                all_count += 1
                if sign not in letters_dic.keys():
                    letters_dic[sign] = 1
                else:
                    letters_dic[sign] += 1
            else:
                pass

    original_text.close()
    return letters_dic, all_count


def analysis_text(letters_value_dic, letters_number):

    analys = open('analysis.txt', 'w')
    analysis_table = []
    table = []
    for elem in letters_value_dic:
        index = round((int(letters_value_dic[elem])/letters_number), 3)
        table.append(f'{1 - index} {elem} {index}')

    table = sorted(table)

    for elem in table:
        elem = elem.split()
        analysis_table.append(elem[1] + ' ' + elem[2] + '\n')

    analysis_table = ''.join(analysis_table)
    analys.write(analysis_table)
    analys.close()
    analys = open('analysis.txt', 'r')
    print(analys.read())
    analys.close()


value_dic, number = letters_value('text.txt')
analysis_text(value_dic, number)
