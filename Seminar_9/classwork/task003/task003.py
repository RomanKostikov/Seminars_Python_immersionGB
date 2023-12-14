# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {'args': args, 'kwargs': kwargs, 'result': result}
            with open(filename, 'a') as file:
                json.dump(data, file)
                file.write('\n')
            return result

        return wrapper

    return decorator


@save_to_json('output.json')
def add_numbers(a, b):
    result = a + b
    return result


result = add_numbers(2, 3)
print(result)  # Выведет: 5
