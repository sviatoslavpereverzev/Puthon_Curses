"""Написать функцию которая возвращает рандомную строку из n элементов"""

from random import choice, choices

my_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890'

def random_str(n):  # функция недописанная
    final_str = ''
    for i in range(int(n)):
        final_str += choice(my_str)
    return final_str

print(random_str(7))




# def my_function(x, y,z):
#
#     return x+y+z
#
# suma = my_function(1,2,3)
#
# suma = suma - 6
#
# print(suma)