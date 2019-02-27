from time import time

"""
В место, огороженное со всех сторон стеной, поместили пару кроликов,
природа которых такова, что любая пара кроликов производит на свет
другую пару каждый месяц, начиная со второго месяца своего существования.
Сколько пар кроликов будет через год?
"""


# 1: 1 + 1 = 2
# 2:     1 + 2 = 3
# 3:         2 + 3 = 5
# 4:             3 + 5 = 8
# 5:                 5 + 8 = 13
# 6:                     8 + 13 = 21
# 7:                         13 + 21 = 34
# 8:                              21 + 34 = 55
# 9:                                   34 + 55 = 89
# ...                                           и т. д.

def rabbits(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        return rabbits(n - 1) + rabbits(n - 2)


# print(rabbits(4))


def fibonachi(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fibonachi(x - 2) + fibonachi(x - 1)




def fib(n):
    fib_1 = 0
    fib_2 = 1
    sum_fin = 0
    if n == 1:
        return fib_1
    if n == 2:
        return fib_2
    if n > 2:
        for i in range(2, n+1):
            sum_fin = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = sum_fin
        return sum_fin

start =time()
print(fibonachi(10))
print(time()-start,'fib_1')

start =time()

print(fib(10))
print(time()-start,'fib_1')


