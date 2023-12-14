# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно

def create_unicode_dictionary(numbers):
    start, end = map(int, numbers.split())
    unicode_dict = {}
    for code in range(start, end + 1):
        unicode_dict[chr(code)] = code
    return unicode_dict


numbers = "1000 2000"
unicode_dict = create_unicode_dictionary(numbers)
print(unicode_dict)
