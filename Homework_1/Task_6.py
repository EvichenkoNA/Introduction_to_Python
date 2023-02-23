""""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали
S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что
Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два
раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""

count = int(input("Введите общее количество сделанных журавликов S "
                  "(число кратное 6): "))
if count % 6 != 0:
    print("Введено некорректное число, повторите ввод.")
else:
    x1 = int(count / 6)  # Сделали Петя и Сережа по отдельности
    x2 = 4 * x1  # Сделала Катя
    print(f"Петя, Катя и Сережа сделали журавликов соответственно: "
          f"{x1} {x2} {x1}")
