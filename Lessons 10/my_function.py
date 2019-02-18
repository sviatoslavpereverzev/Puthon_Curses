def print_hello():  # функция которая ничего не принимает
    print('Hello World')


def print_hello(name, surname):  # функция которая принимает два параметре
    print('Hello', name, surname)
    # print_hello()  # если раскоментировать эту строку то функция будет вызывать саму себя - рекурсия


# print_hello('Vasily', 'Vasilyevich')


def my_sum(x, y):  # функция сравнивающая два числа
    if x > y:
        return 'Больше х'
    elif y > x:
        return 'Больше у'
    else:
        return 'Они равны'


# print(my_sum(2, 3))
# print(my_sum(3, 2))
# print(my_sum(3, 3))


def my_return():
    print('Начало')
    return None
    print('Конец')  # все что назодиться после return не выполняется так как функция прекращает работу


# my_return()

def division(x, y):  # функция, которая делит два числа
    try:
        return x / y
    except ZeroDivisionError:
        return 'Вы делите на ноль '  # при делении на ноль возвращает эту строку


# print(division(6, 3))
# print(division(6, 0))


quit = False  # переменная для прекращения цикла
winner = None  # переменная побелителя
while not quit:  # цикл работает пока quit == False
    print('Здесть наша программа')
    winner = 'X'
    quit = True  # Если нужно прекратить программу то переменной quit присваеваем значение True

print('Победил ', winner)
