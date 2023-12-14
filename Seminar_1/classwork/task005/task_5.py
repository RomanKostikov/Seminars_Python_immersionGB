# Задание №8
# нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#  *
#  ***
#  *****
#  *******
# *********

def draw_tree(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def main():
    rows = int(input("Сколько рядов у ёлки? "))

    draw_tree(rows)


if __name__ == "__main__":
    main()
