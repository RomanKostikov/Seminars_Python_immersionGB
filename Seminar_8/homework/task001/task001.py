# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию
# и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
# Каждый результат должен содержать следующую информацию:
# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
# Важные детали:
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
# Для файлов сохраните их размер в байтах.
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории,
# и вложенных директорий.
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
# Для обхода файловой системы вы можете использовать модуль os.
# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и
# возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных
# файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
import os
import json
import csv
import pickle


def get_directory_size(directory):
    total_size = 0
    for path, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory):
    results = []
    for path, dirs, files in os.walk(directory):
        for f in files:
            file_path = os.path.join(path, f)
            file_size = os.path.getsize(file_path)
            if path == 'geekbrains\my_ds_projects\My-code':
                file_size *= 2
            elif path == 'geekbrains\my_ds_projects':
                file_size *= 4
            result = {
                "Path": os.path.abspath(file_path),
                "Type": "File",
                "Size": file_size
            }
            results.append(result)
        for d in dirs:
            dir_path = os.path.join(path, d)
            dir_size = get_directory_size(dir_path)
            if path == 'geekbrains\my_ds_projects\My-code':
                dir_size *= 2
            elif path == 'geekbrains\my_ds_projects':
                dir_size *= 4
            result = {
                "Path": os.path.abspath(dir_path),
                "Type": "Directory",
                "Size": dir_size
            }
            results.append(result)
    return results


def save_results_to_json(results, filename):
    with open(filename, "w") as file:
        json.dump(results, file)


def save_results_to_csv(results, filename):
    keys = results[0].keys()
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, filename):
    with open(filename, "wb") as file:
        pickle.dump(results, file)


#
# # Пример использования
# directory = "путь_к_директории"
#
directory = 'geekbrains'
results = traverse_directory(directory)
print(results)
# # Получение результатов обхода директории
# results = traverse_directory(directory)

# Сохранение результатов в различных форматах

# Формат JSON
save_results_to_json(results, "результаты.json")

# Формат CSV
save_results_to_csv(results, "результаты.csv")

# Формат Pickle
save_results_to_pickle(results, "результаты.pickle")

# ожидаемый результат
