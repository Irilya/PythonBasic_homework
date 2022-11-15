from typing import Callable


user_check_permissions = ['admin']


def check_permission(permission: str) -> Callable:
    def checking(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                if permission in user_check_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: У пользователя недостаточно прав, '
                      f'чтобы выполнить функцию {func.__name__}')
        return wrapper
    return checking


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
