import re


def get_password_strength(password, user_name):
    list_frequently_passwords = [
        '123456', '12345', 'password', 'DEFAULT', '123456789',
        'qwerty', '12345678', 'abc123', 'pussy', 'password1', '123qwerty']
    list_companies = [
        'Google', 'Yandex', 'Samsung', 'Lg', 'iphone', 'Apple', 'Gmail']
    evaluation = 0
    if re.match('^(?=.*[A-Z]).{6,}$', password):    # 1 регистр верхний
        evaluation += 3
    if re.findall('^(?=.*[a-z]).{6,}$', password):  # 2 регистр нижний
        evaluation += 2
    if re.findall('^(?=.*[0-9]).{6,}$', password):  # 3 цифры
        evaluation += 1
    if re.findall('^(?=.*[!@#$&*]).{6,}$', password):   # 4 спец.символы
        evaluation += 4
    if list_frequently_passwords.count(password):   # 5 словарь
        print('Не используй часто используемые пароли')
        evaluation = 0
    elif re.findall(
            '([0-9]{4}(0[1-9]|1[012])(0[1-9]|1[0-9]|2[0-9]|3[01]))|'
            '((0[1-9]|1[0-9]|2[0-9]|3[01])(0[1-9]|1[012])[0-9]{4})',
            password):  # 6 формат ггггммдд и ддммгггг
        print('Не используй даты')
        evaluation = 0
    elif user_name in password:  # 7 личная информация
        print('Не используй свое имя')
        evaluation = 0
    elif list_companies.count(password):    # 8 словарь
        print('Не используй название компаний')
        evaluation = 0
    elif re.findall('(7|8)([0-9]{10})', password):  # 9 номер телефона
        print('Не используй номер телефона')
        evaluation = 0
    elif len(password) < 6:
        print('Короткий пароль')
        evaluation = 0
    return evaluation

if __name__ == '__main__':
    user_name = input('Введите ваше имя\n')
    password = input('Введите ваш пароль\n')
    evaluation = get_password_strength(password, user_name)
    if not evaluation == 0:
        print('Оценка = {}'.format(evaluation))
    else:
        print('Устраните замечания, чтобы получить оценку')
