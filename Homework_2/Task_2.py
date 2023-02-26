"""
Задание 2.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

num = int(input("Введите целое положительное число: "))
if num <= 0:
    print('Вы ввели не положительное число!')
else:
    max_digit = num % 10
    while num >= 1:
        num = num // 10
        if num % 10 > max_digit:
            max_digit = num % 10
    print(f'Самая большая цифра в числе: {max_digit}')

