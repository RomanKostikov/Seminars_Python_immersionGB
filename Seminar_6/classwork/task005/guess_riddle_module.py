# Задание №4
# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.

# Задание №5
# � Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# � Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.
def guess_riddle(riddles, answers, num_attempts):
    riddle_dict = {}

    for riddle in riddles:
        print("New riddle:", riddle)
        guess = input("Enter your guess: ")

        if guess in answers:
            print("Congratulations! You guessed the riddle.")
            riddle_dict[riddle] = answers
        else:
            print("Sorry, that's not the correct answer.")

    return riddle_dict
