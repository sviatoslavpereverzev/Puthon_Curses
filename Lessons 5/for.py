"""Циклы for"""
for i in range(10):
    print(i)


for _ in range(10):  # '_' -можно использовать, если нам не нужны значения итерируемого объекта
    print('Hello world!')

for x in range(10):
    print('\n')
    for y in range(10):
        print(x, y, end='')
