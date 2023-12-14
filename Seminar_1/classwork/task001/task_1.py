# Работа в консоли в режиме интерпретатора Python(решаем в IDE).
# Решите квадратное уравнение 5x2
# -10x-400=0 последовательно
# сохраняя переменные a, b, c, d, x1 и x2.
# *Попробуйте решить уравнения с другими значениями a, b, c.
import math

a = 5
b = -10
c = -400

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    result = round(x1, 2), round(x2, 2)
elif d == 0:
    x1 = -b / (2 * a)
    result = round(x1, 2)
else:
    result = 'No roots'
print(result)
