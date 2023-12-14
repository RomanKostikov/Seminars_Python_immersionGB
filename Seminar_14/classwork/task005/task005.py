# Задание №5
# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest
from task004_Sem_12 import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_perimeter(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.perimeter(), 30)

    def test_comparison(self):
        rect1 = Rectangle(5, 10)
        rect2 = Rectangle(7, 3)
        self.assertLess(rect2, rect1)


if __name__ == '__main__':
    unittest.main()
