# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


person = Person("Иван", "Иванов", 25)
print(person.full_name())  # Выводит "Иван Иванов"
print(person.age)  # Выводит 25

person.birthday()
print(person.age)  # Выводит 26


# Решение в классе
# class Person:
#
#     def __init__(self, name, last_name, patronymic, age):
#         self.name = name
#         self.last_name = last_name
#         self.patronymic = patronymic
#         self.__age = age
#
#     def birthday(self):
#         self.__age += 1
#
#     def full_name(self):
#         return f'{self.last_name} {self.name} {self.patronymic}'
#
#     def get_age(self):
#         return self.__age
#
#
# person1 = Person('Max', 'Jones', 'Petrovich', 33)
# print(person1.full_name())
# print(person1.get_age())
# person1.birthday()
# print(person1.get_age())