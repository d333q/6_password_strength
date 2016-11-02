import re
import getpass

LIST_FREQUENTLY_PASSWORDS = [
        '123456', '12345', 'password', 'DEFAULT', '123456789',
        'qwerty', '12345678', 'abc123', 'pussy', 'password1', '123qwerty']
LIST_COMPANIES = [
        'Google', 'Yandex', 'Samsung', 'Lg', 'iphone', 'Apple', 'Gmail']


def get_password_strength(password, user_name):
    evaluation = 0
    if re.match('^(?=.*[A-Z]).{6,}$', password):    # 1 регистр верхний
        evaluation += 3
    if re.findall('^(?=.*[a-z]).{6,}$', password):  # 2 регистр нижний
        evaluation += 2
    if re.findall('^(?=.*[0-9]).{6,}$', password):  # 3 цифры
        evaluation += 1
    if re.findall('^(?=.*[!@#$&*]).{6,}$', password):   # 4 спец.символы
        evaluation += 4
    if (len(password) < 6 or
        user_name in password or
        LIST_COMPANIES.count(password) or
        re.findall('(7|8)([0-9]{10})', password) or
        LIST_FREQUENTLY_PASSWORDS.count(password) or
        re.findall(
            '([0-9]{4}(0[1-9]|1[012])(0[1-9]|1[0-9]|2[0-9]|3[01]))|'
            '((0[1-9]|1[0-9]|2[0-9]|3[01])(0[1-9]|1[012])[0-9]{4})',
            password)):
        evaluation = 0
    return evaluation


def print_password_strength(evalution):
    if not evaluation == 0:
        print('Оценка = {}'.format(evaluation))
    else:
        print('Запрещено применять: часто используемые пароли, даты, своё имя,'
              ' название известных компаний, номера телефонов, а также пароли '
              'меньше 6 знаков')


if __name__ == '__main__':
    user_name = input('Введите ваше имя\n')
    password = getpass.getpass('Введите ваш пароль\n')
    evaluation = get_password_strength(password, user_name)
    print_password_strength(evaluation)
