"""Написать функцию которая возвращает рандомную строку из n элементов"""

from random import choice

my_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-()'

print(choice(my_str))


def random_str():  # функция недописанная
    return choice(list(my_str))
