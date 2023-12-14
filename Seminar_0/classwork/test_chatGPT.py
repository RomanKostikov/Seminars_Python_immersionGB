# Написать программу, которая принимает на вход произвольные числа и считает их сумму использовать принципы ООП

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


def sum_numbers(*args):
    total = Number(0)
    for num in args:
        total += num
    return total.value


# Пример использования
print(sum_numbers(Number(1), Number(2), Number(3)))  # выводит 6
print(sum_numbers(Number(4), Number(5), Number(6), Number(7)))  # выводит 22
