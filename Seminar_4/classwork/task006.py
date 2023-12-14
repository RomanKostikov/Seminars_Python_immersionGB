# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def sum_numbers(numbers, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index >= len(numbers):
        end_index = len(numbers) - 1
    return sum(numbers[start_index:end_index + 1])


numbers = [1, 2, 3, 4, 5]
start_index = 1
end_index = 2
result = sum_numbers(numbers, start_index, end_index)
print(result)
