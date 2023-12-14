# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

# class Архив:
#     """
#     Инициализирует новый экземпляр класса.
#
#     Параметры:
#         number (int): Параметр number.
#         string (str): Параметр string.
#
#     Возвращает:
#         None
#     """
#
#     def __init__(self, number, string):
#         self.number = number
#         self.string = string
#         self.number_archive = []
#         self.string_archive = []
#
#         # Store old data from previous instances
#         for instance in Архив.instances:
#             self.number_archive.append(instance.number)
#             self.string_archive.append(instance.string)
#
#         # Add current instance to the list of instances
#         Архив.instances.append(self)
#
#
# # Initialize the list of instances
# Архив.instances = []
# Решение на паре
class Archive:
    """
    Инициализирует новый экземпляр класса Архив.

    Параметры:
        num (int): Число, которое присваивается экземпляру Архив.
        name (str): Строка, которая присваивается экземпляру Архив.

    Возвращает:
        None
    """
    _last = []

    def __init__(self, num: int, name: str):
        self.num = num
        self.name = name
        self.archives_list = Archive._last.copy()
        Archive._last.append(self)

    def __repr__(self) -> str:
        return f"Archive({self.num}, '{self.name}')"


a = Archive(1, 'a')
b = Archive(1, 'b')
c = Archive(1, 'c')

print(a.archives_list)
print(b.archives_list)
print(c.archives_list)
