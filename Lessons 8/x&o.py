board = [
    ['','',''],
    ['','',''],
    ['','','']
]

while True:
    try:
        row = int(input('Введите строку:'))
        column = int(input('Введиите столбик:'))
        print(row, column)
        print(0 == (row or column))
        if row == 0:
            print('Введите координаты от 1 до 3')
            continue
        elif column == 0:
            print('Введите координаты от 1 до 3')
            continue

        if board[row-1][column-1] == '':
            board[row-1][column-1] = 'x'
            break
        else:
            print('Там уже что-то есть, введите снова координаты')
            continue

    except ValueError:
        print('Вы ввели не число ')
        continue
    except IndexError:
        print('Мы вышли за пределы')
        continue
