# Задание №6
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print
# def is_leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return True
#     else:
#         return False


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    year = int(input("Введите год: "))

    if is_leap_year(year):
        result = (year, "год является високосным")
    else:
        result = (year, "год не является високосным")
    print(result)


if __name__ == "__main__":
    main()
