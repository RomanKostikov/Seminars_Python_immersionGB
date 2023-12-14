# Задание №2
# � Создайте модуль с функцией внутри.
# � Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# � Функция выводит подсказки “больше” и “меньше”.
# � Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

# Задание №3
# � Улучшаем задачу 2.
# � Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# � Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.
import random
import sys


def guess_number(lower_bound, upper_bound, num_attempts):
    random_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while attempts < num_attempts:
        guess = int(input("Guess a number between {lower_bound} and {upper_bound}: ".format(lower_bound=lower_bound,
                                                                                            upper_bound=upper_bound)))
        attempts += 1

        if guess == random_number:
            print("Congratulations! You guessed the number.")
            return True
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

    print("Sorry, you ran out of attempts.")
    return False


if __name__ == "__main__":
    if len(sys.argv) == 4:
        lower_bound = int(sys.argv[1])
        upper_bound = int(sys.argv[2])
        num_attempts = int(sys.argv[3])
        guess_number(lower_bound, upper_bound, num_attempts)
    else:
        print("Usage: python guess_number_module.py <lower_bound> <upper_bound> <num_attempts>")
