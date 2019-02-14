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


new_func = f_1()

new_func()

def mull(a, b):
    return a * b


# print(mull(3, 5))


def mull_3(a):
    return a * 3


# print(mull_3(5))


def mull_5(a):
    return a * 5


# print(mull_5(3))
#
# def mull(a):
#     a
#     def f(b):
#         return a * b
#     return f
#
#
# new_mull_3 = mull(3)
# print(new_mull_3(5))

def settings():
    settings = {}
    def add_setings(**kwargs):
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
