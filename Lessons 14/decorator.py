def my_func():
    print('Я функция my_func!')


def deckorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        print('Код перед ней')
        func(*args, **kwargs)
        print('Код после функции')

    return wrapper
#
#
# my_func = deckorator(my_func)
#
# @deckorator
# def my_func_2():
#     print('Я функция my_func_2!')
#
#
# # my_func_2 = deckorator(my_func_2)
#
# my_func_2()
#
# @deckorator
# def mull(a,b):
#     print(f'a *b: {a*b}')
#
#
# print()
# mull(5,3)

def close_print(func):
    def wrapper(*args, **kwargs):
       func('Ничего другого не буду печатать')
    return wrapper

# print = close_print(print)

print('Все что угодно ')


