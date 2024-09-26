# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
from transpore import transpose
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


# transposed_matrix = transpose(matrix)
rows = len(matrix)
cols = len(matrix[0])

# создаем новую матрицу с размерами, поменянными местами
transposed = [[0 for row in range(rows)] for col in range(cols)]
print(matrix)
print(transposed)

# заполняем новую матрицу значениями из старой матрицы
for row in range(rows):
    for col in range(cols):
        transposed[col][row] = matrix[row][col]
print(transposed)




