# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest

from classwork.task001.task001 import remove_non_latin_chars


def test_return_string_without_changes():
    text = "Hello World!"
    result = remove_non_latin_chars(text)
    assert result == "hello world"


def test_return_string_with_case_conversion():
    text = "HeLlO wOrLd"
    result = remove_non_latin_chars(text)
    assert result == "hello world"


def test_return_string_with_punctuation_removal():
    text = "Hello, World!"
    result = remove_non_latin_chars(text)
    assert result == "hello world"


def test_return_string_with_non_latin_chars_removal():
    text = "Привет! Hello! 123"
    result = remove_non_latin_chars(text)
    assert result == " hello "


def test_return_string_with_all_conditions():
    text = "Привет! Hello! 123"
    result = remove_non_latin_chars(text)
    assert result == " hello "


if __name__ == '__main__':
    pytest.main()
