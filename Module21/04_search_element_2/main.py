site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_orig_key(dic, key, d_num):

    if key in dic:
        return dic[key]

    if d_num > 1 or d_num <= - 1:
        for sub_dic in dic.values():
            if isinstance(sub_dic, dict):
                result = search_orig_key(sub_dic, key, d_num - 1)
                if result:
                    break
        else:
            result = None
    else:
        result = None

    return result


origihal_key = input('Введите искомый ключ: ')
choice = input('Хотите ввести максимальную глубину (Y/N)? ')
if choice in ('Y', 'y'):
    depth = int(input('Введите максимальную глубину: '))
else:
    depth = int(- 1)

key_value = search_orig_key(site, origihal_key, depth)
print(f'Значение ключа: {key_value}')
