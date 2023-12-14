# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.
def get_value(dictionary, key, default_value):
    try:
        return dictionary[key]
    except KeyError:
        return default_value


my_dict = {"a": 1, "b": 2, "c": 3}

print(get_value(my_dict, "a", None))  # Вывод: 1
print(get_value(my_dict, "d", 0))     # Вывод: 0

