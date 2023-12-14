# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import unittest

from classwork.task001.task001 import remove_non_latin_chars


class TestRemoveNonLatinChars(unittest.TestCase):
    def test_return_string_without_changes(self):
        text = "Hello World!"
        result = remove_non_latin_chars(text)
        self.assertEqual(result, "hello world")

    def test_return_string_with_case_conversion(self):
        text = "HeLlO wOrLd"
        result = remove_non_latin_chars(text)
        self.assertEqual(result, "hello world")

    def test_return_string_with_punctuation_removal(self):
        text = "Hello, World!"
        result = remove_non_latin_chars(text)
        self.assertEqual(result, "hello world")

    def test_return_string_with_non_latin_chars_removal(self):
        text = "Привет! Hello! 123"
        result = remove_non_latin_chars(text)
        self.assertEqual(result, " hello ")

    def test_return_string_with_all_conditions(self):
        text = "Привет! Hello! 123"
        result = remove_non_latin_chars(text)
        self.assertEqual(result, " hello ")


if __name__ == '__main__':
    unittest.main()
