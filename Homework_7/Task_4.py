"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в
виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86
3 5 32
2 4 6
-1 64 -8
3 5 8 3
8 3 7 1
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух
@@ -25,4 +12,34 @@
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, second_matrix):
        if len(self.matrix) != len(second_matrix.matrix):
            return None
        result = []
        for item in zip(self.matrix, second_matrix.matrix):
            result.append([sum([i, j]) for i, j in zip(*item)])

        return Matrix(result)


m_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)

print(matrix_1)
print()
print(matrix_2)
print('Сумма двух матриц:')
print(matrix_1 + matrix_2)