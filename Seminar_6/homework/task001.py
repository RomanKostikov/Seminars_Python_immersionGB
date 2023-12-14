# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу,
# которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в
# зависимости от результата проверки.
# Пример использования На входе:
# date_to_prove = 15.4.2023
# На выходе:
# True
# На входе:
# date_to_prove = 31.6.2022
# На выходе:
# False
# На входе(на самом деле!!!:
# date_to_prove = '31.6.2022'
# На выходе:
# False
from datetime import datetime


def is_valid_date(date):
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


# date_to_prove = '31.6.2022'
# date_to_prove = '0.5.2022'
# date_to_prove = '12.0.2022'
# date_to_prove = '12.5.-2022'
# date_to_prove = '29.2.2020'
# date_to_prove = '31.12.9999'
# date_to_prove = '32.5.2022'
# date_to_prove = '12.13.2022'
date_to_prove = '29.2.2021'

is_valid = is_valid_date(date_to_prove)
print(is_valid)

