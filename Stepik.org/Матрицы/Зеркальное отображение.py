#Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

#Формат входных данных
#На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел.

#Формат выходных данных
#Программа должна вывести матрицу в которой зеркально отображены элементы относительно горизонтальной оси симметрии.

#Тестовые данные
#Sample Input 1:

#4
#1 2 3 4
#5 6 7 8
#8 6 4 2
#3 4 5 6
#Sample Output 1:

#3 4 5 6
#8 6 4 2
#5 6 7 8
#1 2 3 4
#Sample Input 2:

#3
#1 2 3
#4 5 6
#7 8 9
#Sample Output 2:

#7 8 9
#4 5 6
#1 2 3
#Sample Input 3:

#2
#1 1
#1 1
#Sample Output 3:

#1 1
#1 1

#Решение
n = int(input())
matrix = []
def input_matrix(): #функция заполнения матрицы
    for i in range(n):
        temp = [int(num) for num in input().split()]
        matrix.append(temp)
    return matrix

def print_matrix(matrix, n, width=1): #функция вывода матрицы
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()
matrix = input_matrix()
matrix.reverse() 
print_matrix(matrix, n)

