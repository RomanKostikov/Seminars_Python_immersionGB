# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random
import string

import random
import string

import random
import string

import random
import string


def generate_names(num_names, output_file):
    vowels = 'аеиоуыэюя'
    consonants = 'бвгджзклмнпрстфхцчшщъыьэюя'
    russian_vowels = 'аеиоуыэюя'
    russian_consonants = 'бвгджзклмнпрстфхцчшщъыьэюя'

    with open(output_file, 'w', encoding='UTF-8') as f:
        for _ in range(num_names):
            name = ''
            name += random.choice(russian_vowels).capitalize()
            name += ''.join(random.choices(russian_consonants + vowels + consonants, k=random.randint(3, 4)))
            f.write(name + '\n')


generate_names(10, 'names.txt')

# Решение на семинаре
# from random import randint, choice
#
# VOWELS = list('уеыаоэёяию')
# CONSONANT = list(set([chr(i) for i in range(1072, 1104)]).difference(VOWELS))
#
#
# def create_names(file_name: str, count: int = 10):
#     list_name = []
#     for _ in range(count):
#         name = ''
#         for i in range(randint(4, 7)):
#             name += choice(VOWELS) if i % 2 else choice(CONSONANT)
#         list_name.append(name.title())
#     result = '\n'.join(list_name)
#     with open(file_name, 'w', encoding='UTF-8') as file:
#         file.write(result)
#
# create_names('names.txt')

