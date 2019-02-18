"""Проверяем в какой плоскости находиться точка на координатной оси"""
points = [[2, 3], (-1, 4), (-4, -4), (1, -3), (0, 0)]

for point in points:
    if point[0] > 0 and point[1] > 0:
        print('Находимся в 1 четверти')

    elif point[0] < 0 and point[1] > 0:
        print('Находимся в 2 четверти')

    elif point[0] < 0 and point[1] < 0:
        print('Находимся в 3 четверти')

    elif point[0] > 0 and point[1] < 0:
        print('Находимся в 4 четверти')

    else:
        print('Начало координ')
