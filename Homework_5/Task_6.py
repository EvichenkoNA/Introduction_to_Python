""" В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы."""
import random


def guess_number(number, count=0):
    if count == 10:
        print(f"Вы не угадали. Загаданное число - {number}")
    else:
        try:
            input_number = int(input("Угадайте число от 0 до 100: "))
        except ValueError:
            print("Вы ввели не число!")
            guess_number(number, count)
        else:
            if input_number == number:
                print(f"Вы угадали! Загаданное число - {number}")
                return
            else:
                if number > input_number:
                    print("Загаданное число больше")
                else:
                    print("Загаданное число меньше")
                guess_number(number, count + 1)


random_number = random.randint(0, 100)
guess_number(random_number)