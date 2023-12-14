# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
import random


def guessing_game_decorator(func):
    def wrapper(secret_number, max_attempts):
        if secret_number < 1 or secret_number > 100 or max_attempts < 1 or max_attempts > 10:
            secret_number = random.randint(1, 100)
            max_attempts = random.randint(1, 10)
            print("Переданные числа не входят в указанные диапазоны. Генерируются случайные числа.")

        return func(secret_number, max_attempts)

    return wrapper


@guessing_game_decorator
def create_guessing_game(secret_number, max_attempts):
    attempts = 0

    def guess_number():
        nonlocal attempts
        while attempts < max_attempts:
            attempts += 1
            guess = int(input("Введите вашу догадку: "))
            if guess == secret_number:
                print("Поздравляю, вы угадали число!")
                return
            elif guess < secret_number:
                print("Загаданное число больше вашей догадки.")
            else:
                print("Загаданное число меньше вашей догадки.")

        print("Вы использовали все попытки. Загаданное число было", secret_number)

    return guess_number


game = create_guessing_game(111, 5)
game()
