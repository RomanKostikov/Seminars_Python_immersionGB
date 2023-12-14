# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.
# Возможно, могут помочь друзья так как работают в этой области.
# Возможно, могут помочь родственники так как работают в этой области и могут предложить проект на фриланс.
import os
import json
from typing import Callable
from random import randint
from functools import wraps


def guess_number_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(number_to_guess: int, guesses_count: int):
        func(number_to_guess if 0 < number_to_guess < 101 else randint(1, 100),
             guesses_count if 0 < guesses_count < 11 else randint(1, 10))

    return wrapper


def save_result_to_json(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        path = 'results.json'

        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                file_data = dict(json.load(f))
        else:
            file_data = {}

        result = func(*args, **kwargs)
        file_data[str(result)] = {'args': args}

        for key, value in kwargs.items():
            file_data[str(result)][key] = value

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(file_data, f, indent=2, ensure_ascii=False)

    return wrapper


def count_calls(calls: int) -> Callable:
    def deco(func: Callable) -> Callable:
        results = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal results
            for _ in range(calls):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


@count_calls(3)
@guess_number_decorator
@save_result_to_json
def number_guess(number_to_guess: int, guesses_count: int):
    '''
    Веселая игрушка-угадайка)
    '''
    current_guess = 0

    while current_guess < guesses_count:
        print(f'Осталось {guesses_count - current_guess} попыток')
        guess = int(input('Введите ваше число: '))

        if guess == number_to_guess:
            result = f'Вы выиграли! Вы угадали число {number_to_guess} с {current_guess + 1} попытки!'
            print(result)
            return result

        current_guess += 1
        hints = [f'Больше, чем {guess}', f'Меньше, чем {guess}']
        print(hints[number_to_guess < guess])

    result = f'Вы проиграли! было загадано число {number_to_guess}'
    print(result)
    return result


number_guess(1, 5)
# print(number_guess.__doc__)
# help(number_guess)
