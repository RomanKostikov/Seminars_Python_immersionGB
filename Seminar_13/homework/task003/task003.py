# Управление информацией о сотрудниках и их возрасте
# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный)
# имеет следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым
# числом.
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество,
# Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и
# InvalidAgeError, если данные неверные.
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID
# (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно
# при передаче неверных данных.

class InvalidNameError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidIdError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

        if not self._validate_name(last_name) or not self._validate_name(first_name) or not self._validate_name(
                middle_name):
            raise InvalidNameError(f"Invalid name: {last_name}. Name should be a non-empty string.")

        if not self._validate_age(age):
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")

    def _validate_name(self, name):
        return isinstance(name, str) and len(name) > 0

    def _validate_age(self, age):
        return isinstance(age, int) and age > 0

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, ID):
        super().__init__(last_name, first_name, middle_name, age)
        self.ID = ID

        if not self._validate_id(ID):
            raise InvalidIdError(
                f"Invalid id: {ID}. Id should be a 6-digit positive integer between 100000 and 999999.")

    def _validate_id(self, ID):
        return isinstance(ID, int) and 100000 <= ID <= 999999

    def get_level(self):
        return sum(int(digit) for digit in str(self.ID)) % 7


# Пример использования:
# try:
#     person = Person("Иванов", "Иван", "Иванович", 25)
#     person.birthday()
#     print(f"Возраст: {person.age}")
#
#     employee = Employee("Петров", "Петр", "Петрович", 30, 123456)
#     print(f"Уровень: {employee.get_level()}")
#
# except (InvalidNameError, InvalidAgeError, InvalidIdError) as e:
#     print(f"Ошибка: {str(e)}")

# person = Person("", "John", "Doe", 30)
# print(person)
# Ожидаемый ответ:
# __main__.InvalidNameError: Invalid name: . Name should be a non-empty string.

# person = Person("Alice", "Smith", "Johnson", -5)
# print()
# Ожидаемый ответ:
# __main__.InvalidAgeError: Invalid age: -5. Age should be a positive integer

# employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
# print()
# Ожидаемый ответ:
# __main__.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.

person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
# Ожидаемый ответ:
# 25
