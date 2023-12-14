# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
class FactorialCalculator:
    def __init__(self, k):
        self.k = k
        self.values = []

    def factorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        self.values.append((n, result))
        if len(self.values) > self.k:
            self.values.pop(0)
        return result

    def get_previous_values(self):
        return self.values


calculator = FactorialCalculator(3)
result = calculator.factorial(5)
previous_values = calculator.get_previous_values()
print(result)
print(previous_values)


# решение с пары
# class Factorial:
#
#     def __init__(self):
#         self.storage = []
#         self.last = 1
#         self.count = 0
#
#     def __call__(self, value):
#         if value > self.count:
#             i = self.count
#             while i < value:
#                 self.storage.append(self.last)
#                 self.count +=1
#                 i += 1
#                 self.last = self.last * i
#             self.storage.append(self.last)
#         return self.last
#
#     def get_storage(self):
#         return self.storage
#
#
# if __name__ == '__main__':
#     fact = Factorial()
#     print(fact(5))
#     print(fact.storage)
#     print(fact.get_storage())
#     print(fact(8))
#     print(fact.get_storage())