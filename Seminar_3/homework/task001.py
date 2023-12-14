# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
# На входе:
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
# На выходе, например, один из допустимых вариантов может быть таким:
# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}

def fit_items_to_backpack(items, max_weight):
    backpack = {}
    current_weight = 0
    for item, weight in items.items():
        if current_weight + weight <= max_weight:
            backpack[item] = weight
            current_weight += weight
    return backpack


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
backpack = fit_items_to_backpack(items, max_weight)
# print(backpack)
