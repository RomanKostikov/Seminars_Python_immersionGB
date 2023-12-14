# Задание №5
# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.
def calculate_sum_of_even_numbers(n, e):
    sum_of_even_numbers = 0
    current_number = 1

    while current_number <= n:
        if current_number % 2 == 0 and current_number % e != 0:
            sum_of_even_numbers += current_number
        current_number += 1

    return sum_of_even_numbers


def main():
    n = int(input("Введите значение n: "))
    e = int(input("Введите значение e: "))

    result = calculate_sum_of_even_numbers(n, e)
    print("Сумма чётных элементов от 1 до", n, "исключая кратные", e, "равна:", result)


if __name__ == "__main__":
    main()
