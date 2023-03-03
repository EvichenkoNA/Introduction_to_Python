"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

list_seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето',
                'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
dict_seasons = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна',
                6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень',
                11: 'Осень', 12: 'Зима'}
def find_season_list(month):
    """
    Определяет сезон по номеру месяца. Реализовано через списки
    :param month: номер месяца
    :return: сезон
    """
    return list_seasons[month - 1]

def find_season_dict(mounth):
    """
    Определяет сезон по номеру месяца. Реализовано через словарь
    :param mounth: номер месяца
    :return: сезон
    """
    return dict_seasons[mounth]

try:
    month = int(input('Введите номер месяца: '))
    if month <= 0 or month > 12:
        print('Введите корректное значение месяца!')
    else:
        season_1 = find_season_list(month)
        print(f'Результат через список: {season_1}')
        season_2 = find_season_dict(month)
        print(f'Результат через словарь: {season_2}')
except ValueError:
    print('Введите корректное значение месяца!')