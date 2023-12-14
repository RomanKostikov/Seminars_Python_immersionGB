# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from classwork.task003.task003 import Person


class Employee(Person):
    def __init__(self, first_name, last_name, age, id_number):
        super().__init__(first_name, last_name, age)
        self.id_number = id_number

    @property
    def access_level(self):
        return self.id_number % 7


employee = Employee("Иван", "Иванов", 25, 123456)
print(employee.full_name())  # Выводит "Иван Иванов"
print(employee.age)  # Выводит 25
print(employee.id_number)  # Выводит 123456
print(employee.access_level)  # Выводит 2
