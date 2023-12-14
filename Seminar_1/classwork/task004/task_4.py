# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число.
# Откажитесь от магических чисел
# В коде должны быть один input и один print
# number = int(input("Введите число от 1 до 999: "))
#
# if number < 1 or number > 999:
#     number = int(input("Число должно быть от 1 до 999. Повторите ввод: "))
#
# if len(str(number)) == 1:
#     result = number ** 2
# elif len(str(number)) == 2:
#     digits_product = 1
#     for digit in str(number):
#         digits_product *= int(digit)
#     result = digits_product
# elif len(str(number)) == 3:
#     result = int(str(number)[::-1])
#
# print(result)

def process_number(number):
    if number < 1 or number > 999:
        return "Число должно быть от 1 до 999"

    if number < 10:
        return number ** 2

    if number < 100:
        digit1 = number // 10
        digit2 = number % 10
        return digit1 * digit2

    if number < 1000:
        return int(str(number)[::-1])


def main():
    number = int(input("Введите число от 1 до 999: "))

    result = process_number(number)
    print("Результат:", result)


if __name__ == "__main__":
    main()
