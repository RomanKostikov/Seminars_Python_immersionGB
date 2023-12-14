# Создать функцию sum, которая принимает произвольное количество аргументов и возвращает их сумму.
def summ(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    print(sum(1, 2, 3, 4, 5))


if __name__ == '__main__':
    main()
