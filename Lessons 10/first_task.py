"""Написать функцию которая возвращает дробную часть числа
    округленную до n значений после запятой"""


def after0(digit, n):
    return round(digit % 1, n)


dig = float(input('число:'))
print(after0(dig, 3))
