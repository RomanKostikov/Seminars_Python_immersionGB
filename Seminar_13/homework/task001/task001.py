# Исключение NegativeValueError
# Добавьте в задачу Rectangle, которую писали ранее, исключение NegativeValueError, которое выбрасывается при
# некорректных значениях ширины и высоты, как при создании объекта, так и при установке их через сеттеры.

class NegativeValueError(Exception):
    """
    Исключение, выбрасываемое при некорректных значениях ширины и высоты прямоугольника.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        if width < 0:
            raise NegativeValueError("Ширина должна быть положительной, а не {}".format(width))
        if height is not None and height < 0:
            raise NegativeValueError("Высота должна быть положительной, а не {}".format(height))
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


# try:
#     r1 = Rectangle(-5, 3)
#     print(f"r1 width: {r1.width}, height: {r1.height}")
#     print(f"r1 perimeter: {r1.perimeter()}")
#     print(f"r1 area: {r1.area()}")
#     print()
#
#     r2 = Rectangle(4)
#     print(f"r2 width: {r2.width}, height: {r2.height}")
#     print(f"r2 perimeter: {r2.perimeter()}")
#     print(f"r2 area: {r2.area()}")
#     print()
#
#     r3 = r1 + r2
#     print(f"r3 width: {r3.width}, height: {r3.height}")
#     print(f"r3 perimeter: {r3.perimeter()}")
#     print(f"r3 area: {r3.area()}")
#     print()
#
#     r4 = r3 - r2
#     print(f"r4 width: {r4.width}, height: {r4.height}")
#     print(f"r4 perimeter: {r4.perimeter()}")
#     print(f"r4 area: {r4.area()}")
#     print()
#
#     print(f"r1 < r2: {r1 < r2}")
#     print(f"r1 == r2: {r1 == r2}")
#     print(f"r1 <= r2: {r1 <= r2}")
#     print()
#
#     print(f"r1: {r1}")
#     print(f"r2: {r2}")
#     print(f"r3: {r3}")
#     print(f"r4: {r4}")
#
# except NegativeValueError as e:
#     print(f"Error: {e}")

# r = Rectangle(-2)
# Ожидаемый ответ:
# __main__.NegativeValueError: Ширина должна быть положительной, а не -2
# r = Rectangle(5, -3)
# Ожидаемый ответ:
# __main__.NegativeValueError: Высота должна быть положительной, а не -3
