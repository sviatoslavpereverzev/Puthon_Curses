my_dict = {}  # Создание словаря при помощи цикла for
for i in range(1, 11):
    my_dict[f'key_{i}'] = f'value_{i}'
print(my_dict)

my_dict_2 = {f'key_{i}': f'value_{i}' for i in range(1, 11)}  # Создание словаря припомощи генератора словаря

my_dict_3 = {}  # Создали пустой словарь

for item in my_dict.items():  # item в каждой итерации это кортеж из ключа и значение ('key_1', 'value_1')
    my_dict_2[item[1]] = item[0]
    # my_dict_3['value_1'] = 'key_1'  #Эта запись равносильна той, что будет при первой итерации цикла
print(my_dict_3)
