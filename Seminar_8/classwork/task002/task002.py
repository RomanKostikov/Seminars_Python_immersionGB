# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os

# мое решение (без группировки по уровню)
# def add_user():
#     while True:
#         name = input("Enter name: ")
#         identifier = input("Enter identifier: ")
#         access_level = int(input("Enter access level (1-7): "))
#
#         if access_level < 1 or access_level > 7:
#             print("Invalid access level. Please enter a value between 1 and 7.")
#             continue
#
#         # Check if the JSON file exists
#         if os.path.exists("users.json") and os.stat("users.json").st_size > 0:
#             # Load existing data from JSON file
#             with open("users.json", "r") as file:
#                 data = json.load(file)
#         else:
#             # If the file doesn't exist or is empty, create an empty dictionary
#             data = {}
#
#         # Check if identifier already exists
#         duplicate_identifier = False
#         for users in data.values():
#             if identifier in users:
#                 duplicate_identifier = True
#                 break
#
#         if duplicate_identifier:
#             print("Identifier already exists. Please enter a unique identifier.")
#             continue
#
#         # Add new user to data
#         if access_level not in data:
#             data[access_level] = {}
#         data[access_level][identifier] = name
#
#         # Save updated data to JSON file
#         with open("users.json", "w") as file:
#             json.dump(data, file, indent=4)
#
#         break
#
#
# add_user()

# Решение на паре (группировка по уровню доступа)
import os
import json


def check_access_level(lvl: str) -> bool:
    return not (lvl.isdigit() and 0 < int(lvl) < 8)


def check_user_id(u_data: dict, u_id: int) -> bool:
    id_list = []
    for user in u_data.values():
        id_list.extend(user)
    return u_id in id_list


def main(file_path: str):
    users_data = {}
    if not os.path.exists(file_path):
        data = {}
        with open(file_path, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        with open(file_path, 'r', encoding='UTF-8') as file:
            users_data = json.load(file)

    while True:
        name = input('Введите имя пользователя или Enter для выхода: ')
        if not name:
            break
        u_id = int(input('Введите ID пользователя: '))
        while check_user_id(users_data, u_id):
            u_id = int(input(f'ID {u_id} уже занят, выберите другой ID: '))
        lvl_access = input('Введите уровень доступа пользователя: ')
        while check_access_level(lvl_access):
            lvl_access = input('Ошибка уровня доступа, введите число от 1 до 7: ')
        if lvl_access in users_data:
            users_data[lvl_access][u_id] = name
        else:
            users_data[lvl_access] = {u_id: name}
        with open(file_path, 'w', encoding='UTF-8') as file:
            json.dump(users_data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main('result.json')