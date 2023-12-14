# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.
# На входе:
# frac1 = "1/2"
# frac2 = "1/3
# На выходе:
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6
from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

# Разделение строк на числитель и знаменатель
num1, denom1 = map(int, frac1.split('/'))
num2, denom2 = map(int, frac2.split('/'))

# Вычисление общего знаменателя
common_denom = denom1 * denom2

# Вычисление суммы числителей
sum_num = num1 * denom2 + num2 * denom1

# Вычисление произведения числителей и знаменателей
product_num = num1 * num2
product_denom = denom1 * denom2

# Вывод результатов
print(f"Сумма дробей: {sum_num}/{common_denom}")
print(f"Произведение дробей: {product_num}/{product_denom}")

# Проверочный код

# frac1 = "1/2"
# frac2 = "1/3"

# Преобразование строк в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисление суммы и произведения дробей
sum_fraction = fraction1 + fraction2
product_fraction = fraction1 * fraction2

# Вывод результатов
print(f"Сумма дробей: {sum_fraction}")
print(f"Произведение дробей: {product_fraction}")
