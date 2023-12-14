# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

from functools import total_ordering


class Value:
    @classmethod
    def check_value(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be a number')
        if not value > 0:
            raise ValueError('Value must be greater than 0')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)


@total_ordering
class Rectangle:
    __slots__ = ('_width', '_height')
    width = Value()
    height = Value()

    def __init__(self, width: float, height: float = None):
        self.width = width
        self.height = height if height is not None else width

    def _check_other(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Other object must be a Rectangle")

    def __add__(self, other: "Rectangle"):
        self._check_other(other)
        new_length = self._width + other._width
        new_width = self._height + other._height

        return Rectangle(new_length, new_width)

    def __sub__(self, other: "Rectangle"):
        self._check_other(other)
        if other.perimeter() <= self.perimeter():
            new_length = self._width - other._width
            new_width = self._height - other._height

            return Rectangle(new_length, new_width)

        raise ValueError("Other Rectangle must have less perimeter")

    def __lt__(self, other: 'Rectangle') -> bool:
        self._check_other(other)
        return self.area() < other.area()

    def __repr__(self) -> str:
        return f'Rectangle({self._width}, {self._height})'

    def __str__(self) -> str:
        return f'Прямоугольник со сторонами {self._width} и {self._height}'

    def perimeter(self):
        return (self._width + self._height) * 2

    def area(self):
        return self._width * self._height


rect1 = Rectangle(2, 4)
square1 = Rectangle(4)

print(rect1.perimeter())
print(square1.perimeter())

print(rect1.height)
rect1.height = 10
print(rect1.height)
rect1.height = 21
