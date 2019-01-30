import random

print('Случайное число от 0 до 1:', random.random())
print('Случайное число в заданном диапазоне:', random.randint(1, 10))
my_list = ['A', 'B', 'C']
print('Случайное значение из списка ["A", "B", "C"]:', random.choices(my_list))
