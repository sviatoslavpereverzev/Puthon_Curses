def list_for():
    new_list = []
    for i in range(1, 11):
        new_list.append(i)
    return new_list


dict = {1: 0, 2: 0, 3: 0}

list_1 = [dict[i] for i in range(1, 4)]
set_1 = {x for x in range(1, 11)}
dict_1 = {x: x for x in range(1, 11)}

# print(type(list_1))
# print(list_1)
# print()
# print(type(set_1))
# print(set_1)
# print()
# print(type(dict_1))
# print(dict_1)

#
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#
# print(list((x for x in list_)))

# gen = (x for x in range(10))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

def set_():
    set_1 = set()
    for x in range(1, 21):
        if x % 2 == 0:
            set_1.add(x)
    return set_1


# print(set_())
#
print({x for x in range(1, 21) if x %2==0})



list_key = [f'key_{i}' for i in range(1, 11)]
list_valu = [f'valu_{i}' for i in range(1, 11)]

print(list_key)
print(list_valu)
