# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json

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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("values.json", "w") as f:
            json.dump(self.values, f)


with FactorialCalculator(3) as calculator:
    calculator.factorial(5)
    calculator.factorial(7)
    # другие вычисления