# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды
# # Создание списка с повторяющимися элементами
# my_list = [1, 2, 3, 2, 4, 5, 1, 6, 3, 3, 3]
#
# # Создание пустого списка для уникальных элементов
# unique_list = []
#
# # Создание списка для элементов, которые встречаются дважды
# duplicate_list = []
#
# # Проход по элементам списка
# for item in my_list:
#     # Если элемент уже есть в списке уникальных элементов,
#     # добавляем его в список элементов, которые встречаются дважды
#     if item in unique_list:
#         duplicate_list.append(item)
#     else:
#         # Если элемента еще нет в списке уникальных элементов,
#         # добавляем его в этот список
#         unique_list.append(item)
#
# # Удаление элементов, которые встречаются дважды, из исходного списка
# for item in duplicate_list:
#     while item in my_list:
#         my_list.remove(item)
#
# # Вывод результата
# print("Итоговый список:", my_list)

from random import randint
# решение с пары
my_list = []
for _ in range(10):
    my_list.append(randint(1, 10))
print(my_list)

i = 0
while i < len(my_list):
    target = my_list[i]
    if my_list.count(target) == 2:
        while target in my_list:
            my_list.remove(target)
    else:
        i += 1

print(my_list)
