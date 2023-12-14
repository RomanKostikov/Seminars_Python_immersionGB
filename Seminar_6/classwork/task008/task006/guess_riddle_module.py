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

# Задание №6
# � Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# � Функция формирует словарь с информацией о результатах
# отгадывания.
# � Для хранения используйте защищённый словарь уровня
# модуля.
# � Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# � Для формирования результатов используйте генераторное
# выражение.
_tests_dict = {}


def add_test_result(question: str, guess_number: int) -> None:
    _tests_dict[question] = guess_number


def print_tests_result() -> None:
    results = [f'{question} угадана за {guess} попыток' for question, guess in _tests_dict.items()]
    print(*results, sep='\n')


def test_question(question: str, answers: list[str], guesses: int) -> int:
    current_guess = 1
    answers = [answer.lower() for answer in answers]

    print(question)

    while current_guess <= guesses:
        guess = input('Enter your guess: ').lower()

        if guess in answers:
            return current_guess

        current_guess += 1

    return 0


def run_tests(guesses: int) -> None:
    tests = {
        'Зимой и летом одним цветом': ['елка', 'ёлка', 'ель'],
        'Сидит дед во сто шуб одет': ['капуста', 'лук'],
    }

    for el in tests:
        add_test_result(el, test_question(el, tests[el], guesses))


if __name__ == "__main__":
    # print(test_question('Зимой и летом одним цветом', ['елка', 'ёлка', 'ель'], 5))
    run_tests(3)
    print_tests_result()
