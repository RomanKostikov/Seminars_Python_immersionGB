# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
# и возвращает транспонированную матрицу.
# Пример использования На входе:
# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# На выходе:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
def transpose(matrix):
    transposed_matrix = []

    # Определяем количество строк и столбцов в матрице
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0

    # Создаем пустую транспонированную матрицу
    for i in range(num_cols):
        transposed_row = [0] * num_rows
        transposed_matrix.append(transposed_row)

    # Заполняем транспонированную матрицу элементами из исходной матрицы
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


# Пример использования функции
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transposed_matrix = transpose(matrix)
print(transposed_matrix)
