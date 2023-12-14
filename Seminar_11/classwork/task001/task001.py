# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

# import time
#
#
# class MyString(str):
#     def __init__(self, string, author):
#         super().__init__(string)
#         self.author = author
#         self.creation_time = time.time()
#
#
# # Example usage
# my_string = MyString("Hello, world!", "John")
# print(my_string)  # Output: Hello, world!
# print(my_string.author)  # Output: John
# print(my_string.creation_time)  # Output: Current timestamp        self.time = time

from time import time


# решение на паре
class MyString(str):
    """
    Создает новый экземпляр класса.

    Аргументы:
        cls (type): Класс, для которого создается экземпляр.
        value (str): Значение, которое присваивается экземпляру.
        author (str): Автор экземпляра.

    Возвращает:
        instance: Новый созданный экземпляр.
    """

    def __new__(cls, value: str, author: str):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.creation_time = time()

        return instance


mstr = MyString('qwe', 'Dis_Bro')
print(mstr)
print(mstr.author)
print(mstr.creation_time)
