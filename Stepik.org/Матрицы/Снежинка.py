#Снежинка
#На вход программе подается нечетное натуральное число nn. Напишите программу, которая создает матрицу размером n×n заполнив её символами
#Затем заполните символами * среднюю строку и столбец матрицы, главную и побочную диагональ матрицы.
#Выведите полученную матрицу на экран, разделяя элементы пробелами.

#Формат входных данных
#На вход программе подается нечетное натуральное число n, (n≥3) — количество строк и столбцов в матрице.

#Формат выходных данных
#Программа должна вывести матрицу в соответствии с условием задачи.

#Тестовые данные 
#Sample Input 1:

#5
#Sample Output 1:

#* . * . *
#. * * * .
#* * * * *
#. * * * .
#* . * . *
#Sample Input 2:

#7
#Sample Output 2:

#* . . * . . *
#. * . * . * .
#. . * * * . .
#* * * * * * *
#. . * * * . .
#. * . * . * .
#* . . * . . *
#Sample Input 3:

#11
#Sample Output 3:

#* . . . . * . . . . *
#. * . . . * . . . * .
#. . * . . * . . * . .
#. . . * . * . * . . .
#. . . . * * * . . . .
#* * * * * * * * * * *
#. . . . * * * . . . .
#. . . * . * . * . . .
#. . * . . * . . * . .
#. * . . . * . . . * .
#* . . . . * . . . . *

#Решение
def input_matrix(): #функция заполнения матрицы
    matrix = []
    for i in range(n):
        temp = ['.' for i in range(n)]
        matrix.append(temp)
    return matrix
def print_matrix(matrix, n, width=1): #функция вывода матрицы
    for r in range(n):
        for c in range(n):
            print(str(matrix[c][r]).ljust(width), end=' ')
        print()
n = int(input())
if n % 2 == 1:
    mx = input_matrix()
    for i in range(n):
        for j in range(n):
            if i == j or i + j + 1 ==n or j == n // 2 or i == n // 2:
                mx[i][j] = '*'
    print_matrix(mx, n)
else:
    print('Введите нечетное число')
