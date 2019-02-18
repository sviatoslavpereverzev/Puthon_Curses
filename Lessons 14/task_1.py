from time import time




def time_dec(func):
    def wrapper():
        start = time()
        func()
        end = time()
        time_func = end - start
        print(f'функция: {func.__name__}\nвремя: {time_func}')



    return wrapper

@time_dec
def my_func():
    print(my_func.__name__)
    for i in range(10000):
        i = i ** i
    #print(i)

my_func()