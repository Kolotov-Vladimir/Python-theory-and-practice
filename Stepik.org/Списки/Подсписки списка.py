#Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. Например, [1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4], но список [2, 4] не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. Пустой список — подсписок любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

#На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. Напишите программу, которая выводит список, содержащий все возможные подсписки списка, включая пустой список.

#Формат входных данных
#На вход программе подается строка текста, содержащая символы, отделенные символом пробела.

#Формат выходных данных
#Программа должна вывести указанный список, содержащий все возможные подсписки, включая пустой список в соответствии с примерами.

#Примечание. Порядок списков одинаковой длины должен соответствовать порядку их вхождения в основной список.

#Тестовые данные 
#Sample Input 1:

#a b
#Sample Output 1:

#[[], ['a'], ['b'], ['a', 'b']]
#Sample Input 2:

#a b v
#Sample Output 2:

#[[], ['a'], ['b'], ['v'], ['a', 'b'], ['b', 'v'], ['a', 'b', 'v']]
#Sample Input 3:

#a
#Sample Output 3:

#[[], ['a']]
#Sample Input 4:

#1 2 3 0
#Sample Output 4:

#[[], ['1'], ['2'], ['3'], ['0'], ['1', '2'], ['2', '3'], ['3', '0'], ['1', '2', '3'], ['2', '3', '0'], ['1', '2', '3', '0']]

# Решение
l = [i for i in input().split() if i != ' ']
new = [[]]
count = []
for i in range(len(l)):
    for j in range(len(l)):
        count = l[j:i+j+1]
        if len(count) == i + 1:
            new.append(count)

print(new)

