# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.
# Решение №1 (короткое)
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]  # Вручную создаем список с повторяющимися числами
unique_numbers = list(set(numbers))  # Получаем новый список с уникальными элементами
print(unique_numbers)

# Решение №2 (длинное)
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]  # Вручную создаем список с повторяющимися числами
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)