"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']
for line in words:
    el_bytes = line.encode('utf-8')
    el_str = bytes.decode(el_bytes, 'utf-8')
    print(f" {el_str} - {el_bytes}")
    print()

