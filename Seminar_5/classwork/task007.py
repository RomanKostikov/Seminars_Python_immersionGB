# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».
def generate_primes(n):
    num = 2
    count = 0
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


primes = generate_primes(10)
for prime in primes:
    print(prime)


# Решение на паре
# def gen_simple(num: int):
#     yield 2
#     count = 1
#     number = 3
#     while count < num:
#         # number += 2
#         for dev in range(3, int(number ** 0.5) + 1, 2):
#             # print(number, dev)
#             if not number % dev:
#                 # number += 2
#                 break
#         else:
#             yield number
#             count += 1
#         number += 2
#
#
# print(*gen_simple(100))