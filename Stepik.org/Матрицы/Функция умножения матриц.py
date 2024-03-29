#Функция умножения матриц
def mx_mult(matrix1, matrix2):
    n = len(matrix1)
    k = len(matrix2[0])
    op = len(matrix1[0])
    mx3 = [[0] * k for i in range(n)]
    if len(matrix1[0]) != len(matrix2):
        print("Error: matrices are dimensionally inconsistent!")
        return mx3
    for i in range(n):
        for j in range(k):
            for x in range(op):
                mx3[i][j] += matrix1[i][x] * matrix2[x][j]
    return mx3

# Импорт библиотеки numpy для работы с матрицами.
import numpy as np

matrix1 = np.array([[1,1,1], [2,2,2], [3,3,3]])
matrix2 = np.array([[1,2,3], [4,5,6], [7,8,9]])

result = matrix1.dot(matrix2)

for row in result:
    for column in row:
        print(str(column).ljust(3), end=" ")
    print()
    
#Решение вручную
def mx_mult(matrix1, matrix2):
    n = len(matrix1)
    k = len(matrix2[0])
    op = len(matrix1[0])
    mx3 = [[0] * k for i in range(n)]
    if len(matrix1[0]) != len(matrix2):
        print("Error: matrices are dimensionally inconsistent!")
        return mx3
    for i in range(n):
        for j in range(k):
            for x in range(op):
                mx3[i][j] += matrix1[i][x] * matrix2[x][j]
    return mx3
a = [[1, -1, 0], [3, -4, 2]]
b = [[1, 2], [3, 4], [5, 6]]
mx = mx_mult(a, b)
for i in range(len(mx)):
    for j in range(len(mx[i])):
        print(mx[i][j], end=' ')
    print()
