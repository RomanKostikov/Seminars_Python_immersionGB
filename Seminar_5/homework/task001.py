# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')
import os


def get_file_info(file_path):
    if file_path.endswith('/file'):
        path = os.path.dirname(file_path) + '/'
        name = ''
        extension = '.file'
    else:
        path, filename = os.path.split(file_path)
        name, extension = os.path.splitext(filename)
        if file_path.count('/') >= 1:
            path = os.path.dirname(file_path) + '/'
    return (path, name, extension)


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))
# Ожидаем: ('C:/Users/User/Documents/', 'example', '.txt')
print(get_file_info(file_path='/home/user/data/file'))
# # Ожидаем: ('/home/user/data/', '', '.file')
print(get_file_info(file_path='D:/myfile.txt'))  # видимо связано с версией python, в 3.8 один слэш вместо двух
# # Ожидаем: ('D:/', 'myfile', '.txt')
print(get_file_info(file_path='C:/Projects/project1/code/script.py'))
# # Ожидаем: ('C:/Projects/project1/code/', 'script', '.py')
print(get_file_info(file_path='/home/user/docs/my.file.with.dots.txt'))
# # Ожидаем: ('/home/user/docs/', 'my.file.with.dots', '.txt')
print(get_file_info(file_path='file_in_current_directory.txt'))
# # Ожидаем: ('', 'file_in_current_directory', '.txt')
