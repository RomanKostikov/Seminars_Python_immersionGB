# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# На входе:
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе:
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
def key_params(**kwargs):
    dict = kwargs
    new_dict = {}

    # Обрабатываем позиционные аргументы
    for key in dict:
        try:
            int(dict[key])
            new_dict[dict[key]] = key
        except:
            new_dict[str(dict[key])] = key
    return new_dict


# Пример использования функции
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
