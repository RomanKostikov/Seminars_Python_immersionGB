# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

import random


def create_guessing_game(max_attempts):
    secret_number = random.randint(1, 100)
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


game = create_guessing_game(5)
game()
