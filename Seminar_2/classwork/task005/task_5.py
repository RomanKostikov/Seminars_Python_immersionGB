# Задание №5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.
import cmath


def solve_quadratic_equation(a: float, b: float, c: float):
    discriminant = (b ** 2) - (4 * a * c)
    sqrt_discriminant = cmath.sqrt(discriminant)

    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)

    return root1, root2


# Пример использования
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

root1, root2 = solve_quadratic_equation(a, b, c)

print(f"Корень 1: {root1}")
print(f"Корень 2: {root2}")
