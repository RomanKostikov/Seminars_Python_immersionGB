# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import decimal
import math


def calculate_circle_properties(diameter: decimal.Decimal):
    decimal.getcontext().prec = 42
    radius = diameter / 2
    area = decimal.Decimal(math.pi) * (radius ** 2)
    circumference = decimal.Decimal(2 * math.pi) * radius
    return area, circumference


# Пример использования
diameter = decimal.Decimal(input("Введите диаметр круга: "))
area, circumference = calculate_circle_properties(diameter)
print(f"Площадь круга: {area}")
print(f"Длина окружности: {circumference}")
