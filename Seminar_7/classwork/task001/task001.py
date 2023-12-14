# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции
import random


# def fill_file(filename, num_lines):
#     with open(filename, 'a') as file:
#         for _ in range(num_lines):
#             int_num = random.randint(-1000, 1000)
#             float_num = random.uniform(-1000, 1000)
#             file.write(f'{int_num}|{float_num}\n')
#
#
# fill_file('myfile.txt', 10)
#
MIN_VALUE = -1000
MAX_VALUE = 1000


#  Задача в классе решаем
import os
from random import randint, uniform
def file_creator(file_name: str, count: int):
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='UTF-8') as file:
            file.write('')
    for _ in range(count):
        row = f'{randint(MIN_VALUE, MAX_VALUE)} | {uniform(MIN_VALUE, MAX_VALUE)}' + '\n'
        with open(file_name, 'a', encoding='UTF-8') as file:
            file.write(row)


file_creator('example.txt', 5)