# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

from functools import total_ordering


@total_ordering
class Rectangle:
    __slots__ = ['_width', '_height'] # экономим память

    def __init__(self, width: float, height: float = None):
        if not self._check_value(width):
            raise ValueError(f'Invalid value for width: {width}')
        self._width = width
        self._height = height if self._check_value(height) else width

    def _check_value(self, value) -> bool:
        if isinstance(value, (float, int)):
            if value > 0:
                return True
        return False

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if self._check_value(value):
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if self._check_value(value):
            self._height = value

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
rect1.height = -1
