
def check_password(password):


    count = 0
    count_letter = 0
    if len(password) >= 8:
        for sign in password:
            if sign.isdigit():
                count += 1
            elif sign == sign.upper():
                count_letter += 1
    if count >= 3 and count_letter >= 1:
        return True
    else:
        return False


while True:
    password = input('Придумайте пароль: ')
    check_password(password)
    if check_password(password) == False:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break






