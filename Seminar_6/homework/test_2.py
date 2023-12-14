# Решение с перемешиванием от Alexa
import itertools
import random


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in itertools.combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


def generate_boards():
    board_list = []
    succeessful_placements = 0
    count = 0
    set_queens_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    set_queens_2 = [1, 2, 3, 4, 5, 6, 7, 8]
    while succeessful_placements < 4:
        queens = [(set_queens_1[i], set_queens_2[i]) for i in range(0, 8)]
        count += 1
        # print(count)
        if check_queens(queens):
            board_list.append(queens)
            succeessful_placements += 1
        random.shuffle(set_queens_2)
        random.shuffle(set_queens_1)
    return board_list


print(generate_boards())
board_list = generate_boards()
if len(board_list) != 4:
    print("Вы собрали не то количество комбинаций")
else:
    print("Отлично!")
