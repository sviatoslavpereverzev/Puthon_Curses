distance_NY = {
    'Washington': 250,
    'Miami': 1562,
    'Los Angeles': 3062,
    'Las Vegas': 2750,
    'San Francisco': 2437,
}


def func1(dict):
    my_dict = {}
    for key in dict:
        my_dict[key] = round(dict[key] * 1.6, 2)
    return my_dict


def func2(dict):
    return {key: round(dict[key] * 1.6, 2) for key in dict}


def func3(dict):
    return list(map(lambda key: round(dict[key] * 1.6, 3), dict))


def func4(data):
    return dict(map(lambda item: (item[0], round(item[1] * 1.6, 3)), data.items()))


print(func1(distance_NY))
print(func2(distance_NY))
print(func4(distance_NY))
print(func3(distance_NY))
