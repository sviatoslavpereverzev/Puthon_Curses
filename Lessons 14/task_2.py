from time import time

data = {}
print(time())

def time_dec(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        time_func = end - start
        print(f'функция: {func.__name__}\nвремя: {time_func}')

    return wrapper

def log_data(func):
    def wrapper(*args, **kwargs):
        data[func.__name__] = [args, kwargs]
        func()

    return wrapper


@log_data
def f_1(*args, **kwargs):
    pass


@log_data
@time_dec
def f_2(*args, **kwargs):
    pass


@log_data
@time_dec
def f_3(*args, **kwargs):
    for i in range(10000):
        i = i ** i


f_1()
f_2(1, 2, 3, name="olya", age=22)
f_3(name='Danil')
print(data)
