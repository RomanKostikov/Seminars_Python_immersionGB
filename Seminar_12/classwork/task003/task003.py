# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1

class FactorialGenerator:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 1, start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        for num in range(self.start, self.stop + 1, self.step):
            yield self.calculate_factorial(num)

    def calculate_factorial(self, num):
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial


generator = FactorialGenerator(1, 5, 1)
for factorial in generator:
    print(factorial)
