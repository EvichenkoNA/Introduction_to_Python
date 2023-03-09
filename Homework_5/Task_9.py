"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя
использовать циклы.
"""


def sum_of_num(first_num, second_num):
    if second_num == 0:
        return first_num
    else:
        return sum_of_num(first_num + 1, second_num - 1)


try:
    first_input_num = int(input("Введите первое число: "))
    second_input_num = int(input("Введите второе число: "))
    if first_input_num < 0 or second_input_num < 0:
        raise ValueError
except ValueError:
    print("Вы ввели отрицательное число!")
else:
    print("Ответ: ", sum_of_num(first_input_num, second_input_num))
