# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов

import doctest
import re


def remove_non_latin_chars(text):
    """
    Removes all non-Latin alphabet characters and spaces from a text.
    Returns the result in lowercase.

    >>> remove_non_latin_chars("Hello World!")
    'hello world'
    >>> remove_non_latin_chars("HeLlO wOrLd")
    'hello world'
    >>> remove_non_latin_chars("Hello, World!")
    'hello world'
    >>> remove_non_latin_chars("Привет! Hello! 123")
    ' hello '
    >>> remove_non_latin_chars("Привет! Hello! 123")
    ' hello '
    """

    cleaned_text = re.sub('[^a-zA-Z ]', '', text)
    return cleaned_text.lower()


doctest.testmod()
