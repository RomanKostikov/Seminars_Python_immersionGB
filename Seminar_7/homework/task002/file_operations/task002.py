import os

# # Путь к директории, где находится пакет file_operations
# package_directory = "/path/to/file_operations"
#
# # Создание директории, если она не существует
# if not os.path.exists(package_directory):
#     os.makedirs(package_directory)
#
# # Путь к файлу __init__.py
# init_file_path = os.path.join(package_directory, "__init__.py")

# Запись функции rename_files в файл __init__.py
with open('__init__.py', "w") as init_file:
    init_file.write('''def rename_files''')

# print(f"Файл {init_file_path} успешно создан и функция rename_files записана в него.")

with open("__init__.py", "r") as init_file:
    code = init_file.read()

function_names = [
    "def rename_files"
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")

# Ожидаемый ответ:
# Функция def rename_files найдена в файле __init__.py
# Ошибка:
# Traceback (most recent call last):
#   File "3BLIVYP3DQA96P7ZJXWL.py", line 8, in <module>
#     from .file_operations import rename_files
# ImportError: attempted relative import with no known parent package
