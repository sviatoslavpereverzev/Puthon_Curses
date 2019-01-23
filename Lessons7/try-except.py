while True:
    try:
        x = int(input('Введите число на которое делите:\n'))
        print(2 / x)
    except ValueError:
        print('Вы вели не число!')
    except ZeroDivisionError:
        print('Вы делите на ноль')
    else:
        print('Все хорошо')
    finally:
        print('Выполниться в любом случае')