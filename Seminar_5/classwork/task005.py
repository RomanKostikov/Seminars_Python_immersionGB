# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.
#
# print(*(num if num % 3 != 0 and num % 5 != 0 else "Fizz" if num % 3 == 0 else "Buzz" if num % 5 == 0 else "FizzBuzz"
#         for num in range(1, 101)))
print(*[[i, "Fizz", "Buzz", "FizzBuzz"][(i % 3 == 0) + (i % 5 == 0) * 2] for i in range(1, 101)])

# for i in int_lst:
#     if not i % 15:
#         print("FizzBuzz")
#     elif not i % 5:
#         print("Buzz")
#     elif not i % 3:
#         print("Fizz")
#     else:
#         print(i)

# print(*int_lst)
