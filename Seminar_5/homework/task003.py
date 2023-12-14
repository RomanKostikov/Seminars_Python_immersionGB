# Создайте функцию генератор чисел Фибоначчи fibonacci.
# Пример использования.
# На входе:
# f = fibonacci()
# for i in range(10):
#     print(next(f))
# На выходе:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()
for i in range(10):
    print(next(f))
