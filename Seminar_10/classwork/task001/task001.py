# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2


circle = Circle(5)
circumference = circle.calculate_circumference()
area = circle.calculate_area()
print("Circumference:", circumference)
print("Area:", area)
