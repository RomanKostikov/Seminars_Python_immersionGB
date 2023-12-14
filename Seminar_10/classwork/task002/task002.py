# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None else width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


rectangle = Rectangle(4, 5)  # Creates a rectangle with length 4 and width 5
print(rectangle.perimeter())  # Output: 18
print(rectangle.area())  # Output: 20
