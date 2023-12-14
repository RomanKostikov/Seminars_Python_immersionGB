# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно
def get_binary_string(num: int) -> str:
    binary_digits = []
    while num > 0:
        binary_digits.append(str(num % 2))
        num //= 2
    binary_digits.reverse()
    return ''.join(binary_digits)


def get_octal_string(num: int) -> str:
    octal_digits = []
    while num > 0:
        octal_digits.append(str(num % 8))
        num //= 8
    octal_digits.reverse()
    return ''.join(octal_digits)


# Пример использования
number = int(input("Введите целое число: "))
binary_string = get_binary_string(number)
octal_string = get_octal_string(number)
print(f"Двоичное представление: {binary_string}")
print(f"Восьмеричное представление: {octal_string}")
