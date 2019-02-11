from random import choice, choices

"""Функция которая возвращает рандомную строку длинной n,
    в которой длина первого элемента = 1 а кажый следующий на один символ длиннее"""


def random_list(n):
    list_1 = []
    data_str = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(n):
        ch = choices(data_str, k=i + 1)
        join_str = ''.join(ch)
        list_1.append(join_str)
    return list_1


print(random_list(10))

"""Функция принимает список и возвращает рассортированный """


def unsort_list(sort_list):
    new_list = []
    num = len(sort_list)
    for i in range(num):
        ch = choice(sort_list)
        new_list.append(ch)
        sort_list.remove(ch)
    return new_list


print(unsort_list(random_list(10)))
