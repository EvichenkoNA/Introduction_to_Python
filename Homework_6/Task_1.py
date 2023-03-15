"""
Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

a1 = int(input('Введите первый член арифметической прогрессии: '))
d = int(input('Введите разность арифметической прогрессии: '))
n = int(input('Введите количество элементов арифметической прогрессии: '))

# традиционыый итератор с функцией append
for i in range(n):
    print(a1 + i * d)

# List Comprehension
list_1 = [a1 + i * d for i in range(n)]
print(list_1)