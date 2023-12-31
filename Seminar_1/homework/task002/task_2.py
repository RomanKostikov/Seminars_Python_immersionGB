# Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если это число натуральное и делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. Если подается отрицательное число или число более ста тысяч, выведите на экран сообщение: "Число должно быть больше 1 и меньше 100000".
#
# Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.
# На входе:
# num = 2
# На выходе:
# 2 является простым числом

num = int(input("Введите число: "))

if num <= 1 or num > 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} является простым числом")
    else:
        print(f"{num} является составным числом")
