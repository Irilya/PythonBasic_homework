import zipfile


def letters_analysis(zfile):

    roman_text_zip = zipfile.ZipFile(zfile, 'r')
    path = ''
    for file_info in roman_text_zip.infolist():
        path = file_info.filename
    roman = open(roman_text_zip.extract(path), 'r', encoding='utf-8')
    letters_value = {}
    for line in roman:
        for sign in line:
            if sign.isalpha():
                if sign not in letters_value:
                    letters_value[sign] = 1
                else:
                    letters_value[sign] += 1
    roman.close()
    roman_text_zip.close()

    return letters_value


def sorted_letter_table(letters_dic):

    value_table = []
    letters_count = sorted(letters_dic.values())
    for item in letters_count:
        for key, value in letters_dic.items():
            new_str = f'{key} - {value}\n'
            if value == item and new_str not in value_table:
                value_table.append(new_str)

    value_table = ''.join(value_table)
    print(value_table)
    analys = open('letters_table.txt', 'w')
    analys.write(value_table)
    analys.close()


dic_letters = letters_analysis('voyna-i-mir.zip')
sorted_letter_table(dic_letters)
