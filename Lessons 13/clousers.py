"""В функции f_1 мы прописали новую функцию f_2 а потом ее возвращаем"""


def f_1():
    print('Я функция f_1')

    def f_2():
        print('Я функция f_2')

    return f_2


def f_1():
    var = 'Я переменная, которую надо сохранить'
    var_2 = 'Я вторая переменная'

    def f_2():
        print(var, var_2)

    return f_2


f_1  # f_1- это просто название функции
f_1()  # для того чтоб вызвать функцию мы должны поставть '()'
new_func_1 = f_1  # new_func_1 та же функция f_1, просто мы к ней можем обращаться через new_func_1
new_func_2 = f_1()  # а new_func_2- это у нас прочто None потому что мы возвращаем результат функции f_1()
new_func_1()  # вызоы фунуции f_1 уже с другим названием

"""функция которая просто перемножает два числа"""
def mull(a, b):
    return a * b

# print(mull(3, 5))

"""Функция умнжающая число на 3"""
def mull_3(a):
    return a * 3

# print(mull_3(5))

"""Функция умнжающая число на 5"""
def mull_5(a):
    return a * 5

# print(mull_5(3))

"""Если мы хотим написать функцию, которая умножает число на 7, то прийдется писать новую функцию
    Давайте напишем функцию которая поможет нам на любом этапе нашей программы написать новую
    функцию для умножения на конкретное число"""

def mull(a):
    a  # это я написал просто для вас чтоб вы помнили, что пока функция не завершила свою работу
       # ее переменые остаются нам доступны
    def f(b):
        return a * b
    return f

# new_mull_3 = mull(3)  # здесь мы передаем в фунцию mull значение 3 и оно там сохраняется и возвращает функуию f
# print(new_mull_3(5))  # здесь мы уже вызываем функцию f с значением 5 и она нам возвращает 3*5


"""Эта функция позволеет на любом этапе программы создать словарь с настройками и
    добавлять в него значения"""

def settings():
    settings = {}
    def add_setings(**kwargs):  # kwargs - это словарь со значениемя
        nonlocal settings
        if not kwargs:
            return settings
        settings.update(kwargs)
        # settings[key] = value
        return settings

    return add_setings


setings_monitor = settings()

setings_monitor(Monitor=True, Разрешение='1280x768', Матрица='IPS')
# print(setings_monitor())


# dict_ = setings_monitor('Матрица', 'IPS')
# print(dict_)


# settings_hardware = settings()
# print(settings_hardware('Процессор', 'Inel Core i7'))
