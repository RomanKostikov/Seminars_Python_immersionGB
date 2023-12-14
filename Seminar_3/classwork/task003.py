# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа
# Создание кортежа с элементами разных типов
my_tuple = (42, "Hello", 3.14, True, [1, 2, 3], {"name": "John"})

# Создание пустого словаря
result_dict = {}

# Проход по элементам кортежа
for item in my_tuple:
    # Получение типа элемента
    item_type = type(item)

    # Проверка, есть ли тип в словаре
    if item_type in result_dict:
        # Если тип уже есть в словаре, добавляем элемент в соответствующий список
        result_dict[item_type].append(item)
    else:
        # Если типа нет в словаре, создаем новую запись со списком, содержащим элемент
        result_dict[item_type] = [item]

# Вывод результата
for item_type, item_list in result_dict.items():
    print(f"{item_type}: {item_list}")
