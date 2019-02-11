# argument_1,argument_2- не обязательные аргументы у которых есть значение по умолчанию
def my_function(argument_1='Здравствуйте', argument_2=' ребятки'):
    print(argument_1, argument_2)


# my_function('Привет', 'Другой аргумент')

mix_list = [2, 5, 12, 4, 6, 1]


def my_sort(list, reverse=False):  # усли reverse=True, то наша функция верет перевернутый список
    if reverse:
        return sorted(list)[::-1]
    else:
        return sorted(list)


# print(my_sort(mix_list, True))

# аргументы с значением по умолчанию всегда должны быть после аргументов,
# значение которых мы должны передать
def my_function(argument_1, argument_2=2, argument_3=3):
    print(argument_1, argument_2, argument_3)


"""Функция, которая подсчитывает сумму всех элементов одного списка"""


def summa_list(my_list):
    summa = 0
    for value in my_list:
        print(value)
        summa += value
    return summa


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_2 = [x for x in range(10, 21)]

# print(summa_list(my_list))

"""Функция, которая подсчитывает сумму всех элементов двух списков"""


def summa_list_2(my_list_1, my_list_2):
    summa = 0
    for g in my_list_1:
        summa += g
    for h in my_list_2:
        summa += h
    return summa


summa_list_2([1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 5, 7])

"""Функция, которая подсчитывает сумму всех элементов любого колличества списков
    используя *args мы можем передать любое колличество неименнованых параметров"""


def summa_list_3(*args):
    summ = 0
    for arg in args:
        for value in arg:
            summ += value
    return summ


# print(summa_list_3(my_list_2, my_list, [1, 2, 4, 5, 6, 7, 8, 9, ]))


""" Сортировка Пузырьком"""
my_list = [x for x in range(10)[::-1]]

print(my_list)


def sort_bubble(list):
    for _ in range(len(list)):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]


sort_bubble(my_list)
print(my_list)
