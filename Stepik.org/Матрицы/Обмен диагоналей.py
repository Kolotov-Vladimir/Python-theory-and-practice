#Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали
#при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).

#Формат входных данных
#На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

#Формат выходных данных
#Программа должна вывести матрицу с элементами главной и побочной диагонали, поменявшимися своими местами.

#Тестовые данные
#Sample Input 1:

#3
#1 2 3
#4 5 6
#7 8 9
#Sample Output 1:

#7 2 9 
#4 5 6 
#1 8 3 
#Sample Input 2:

#2
#1 2
#4 5
#Sample Output 2:

#4 5
#1 2
#Sample Input 3:

#5
#2 2 3 1 3
#4 6 6 7 5
#7 8 9 7 8
#4 5 6 4 5
#1 2 3 1 2
#Sample Output 3:

#1 2 3 1 2
#4 5 6 4 5
#7 8 9 7 8
#4 6 6 7 5
#2 2 3 1 3

#Решение
# put your python code here

n = int(input())
matrix = []
def input_matrix(): #функция заполнения матрицы
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix

def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
matrix = input_matrix()
for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][i], matrix[n - i -1][i] = matrix[n - i -1][i], matrix[i][i]
print_matrix(matrix, n)

