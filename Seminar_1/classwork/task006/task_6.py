# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
def print_multiplication_table():
    print("Таблица умножения:".center(40))
    for i in range(2, 10):
        for j in range(2, 6):
            result = i * j
            print(f"{i} x {j} = {result}".ljust(15), end="")
        print()

    print()

    for i in range(2, 10):
        for j in range(6, 10):
            result = i * j
            print(f"{i} x {j} = {result}".ljust(15), end="")
        print()


def main():
    print_multiplication_table()


if __name__ == "__main__":
    main()
