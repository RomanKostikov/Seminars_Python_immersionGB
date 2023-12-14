# Задание №4
# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.
def guess_riddle(riddle, answers, num_attempts):
    for attempt in range(1, num_attempts + 1):
        print("Attempt", attempt)
        guess = input("Enter your guess: ")

        if guess in answers:
            print("Congratulations! You guessed the riddle.")
            return attempt

    print("Sorry, you ran out of attempts.")
    return 0
