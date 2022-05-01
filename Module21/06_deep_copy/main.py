import json
import copy


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def rename_new_site(structure, key, name):

    if key in structure:
        structure.pop(key)
        structure[key] = name
        return structure

    for sub_str in structure.values():
        if isinstance(sub_str, dict):
            result = rename_new_site(sub_str, key, name)
            if result:
                break
    else:
        result = None
        return result


site_original = copy.deepcopy(site)
site_quantity = int(input('Сколько сайтов: '))
while site_quantity != 0:
    site_name = input(f'\nВведите название продукта для нового сайта: ')
    print(f'\nСайт для {site_name}:\n')

    rename_new_site(site, name=f'Куплю/продам {site_name} недорого', key='title')
    rename_new_site(site, name=f'У нас самая низкая цена на {site_name}', key='h2')

    print(json.dumps(site, indent=4, sort_keys=True, ensure_ascii=False))
    site_quantity -= 1
