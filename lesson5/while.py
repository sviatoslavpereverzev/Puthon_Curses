"""Делаем цикл while, который будет повторяться 10 раз"""
x = 0
while x < 10:
    print(x)
    x += 1


""" Разбираемся для чего нужны except и break в циклах while и for"""
while True:
    x = input('Введите букву')
    for a in 'Hello world':
        if a == x:
            print('Такая буква есть!')
            break
    else:
        print('Такой буквы нет!')
