# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.
# Словарь с вещами, взятыми друзьями в поход
items = {
    'Друг 1': ('Тент', 'Спальник', 'Фонарик', 'Кружка'),
    'Друг 2': ('Тент', 'Фонарик', 'Компас', 'Палатка'),
    'Друг 3': ('Тент', 'Спальник', 'Кружка', 'Палатка'),
    'Друг 4': ('Тент', 'Спальник', 'Кружка', 'Палатка', 'Фонарик'),
}

# Какие вещи взяли все четыре друга
common_items = set.intersection(*[set(items[friend]) for friend in items])
print("Вещи, взятые всеми четырьмя друзьями:", common_items)

# Какие вещи уникальны, есть только у одного друга
unique_items = set.union(*[set(items[friend]) for friend in items]) - common_items
print("Уникальные вещи, есть только у одного друга:", unique_items)

# Какие вещи есть у всех друзей кроме одного
for friend in items:
    other_friends = set(items.keys()) - {friend}
    shared_items = set.intersection(*[set(items[f]) for f in other_friends])
    missing_items = shared_items - set(items[friend])
    if missing_items:
        print(f"У всех друзей кроме {friend} есть вещи:", missing_items)

# Решение на паре
# friends = {'Паша': ('котелок', 'нож', 'еда', 'одеяло'),
#            'Настя': ('котелок', 'нож', 'мяч', 'топор'),
#            'Коля': ('котелок', 'вода', 'еда', 'топор'),
#            'Игорь': ('вода', 'еда', 'топор', 'нож', 'мяч')}
#
# all_things = set()
# for friend in friends.values():
#     all_things.update(set(friend))
# print('Вещи, которые есть у всех: ')
# print(", ".join(list(all_things)))
#
# one_except_all = {}
# for current_friend, inventory in friends.items():
#     inventory = set(inventory)
#     for friend, values in friends.items():
#         if current_friend != friend:
#             inventory.difference_update(values)
#     if inventory:
#         one_except_all[current_friend] = list(inventory)
#
# print('\nУникальные вещи, которые есть  только у одного:')
# for name, values in one_except_all.items():
#     print(f'{name} - {", ".join(values)}')
#
# all_except_one = {}
# for current_friend, inventory in friends.items():
#     inventory = all_things.difference(inventory)
#     for friend, values in friends.items():
#         if current_friend != friend:
#             inventory.intersection_update(values)
#     if inventory:
#         all_except_one[current_friend] = list(inventory)
#
# print('\nВещи, которые есть у всех, кроме одного:')
# for name, values in all_except_one.items():
#     print(f'{name} - {", ".join(values)}')
