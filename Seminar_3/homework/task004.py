# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# На входе:
# lst = [1, 1, 2, 2, 3, 3]
# На выходе:
# [1, 2, 3]
# lst = [1, 1, 2, 2, 3, 3]
# lst = [1, 2, 3, 4, 5]
# lst = [1, 2, 3, 2, 4, 5, 4]
lst = [1, 2, 3, 4, 5, 6, 7]
# Используем список для хранения дублирующихся элементов
duplicates = []

# Используем множество для проверки наличия дубликатов
unique_elements = set()

for element in lst:
    if element in unique_elements:
        if element not in duplicates:
            duplicates.append(element)
    else:
        unique_elements.add(element)

print(duplicates)
