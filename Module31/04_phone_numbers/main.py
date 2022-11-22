import re


tel_list = ['9999999999', '999999-999', '99999x9999', '8978555555', '7983555555', '898888']

tel_pattern = re.compile(r'\b[89]\d?\d{9}\b')
count = 0
for string in tel_list:
    count += 1
    if len(tel_pattern.findall(string)) > 0:
        print(f'{count}-й номер: всё в порядке')
    else:
        print(f'{count}-й номер: не подходит')
