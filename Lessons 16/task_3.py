# list_key = [f'key_{i}' for i in range(1, 11)]
# list_valu = [f'valu_{i}' for i in range(1, 5)]
#
#
# def dict_1():
#     dict_1 = {}
#     for i in range(len(list_key)):
#         dict_1[list_key[i]] = list_valu[i]
#     return dict_1
#
#
# # print({list_key[i]:list_valu[i] for i in range(len(list_key))})
#
# list_1 = [1, 2, 3, 4]
# list_2 = ['a', 'b', 'c', 'd']
# list_3 = ['val_1', 'val_2', 'val_3']
# print(list(zip(list_1, list_2, list_3)))
#
# print({key:value for key,value in zip(list_key,list_valu) })


def f(valu):
    return True if valu % 5 == 0 else False


x = 10 if False else 5
# print(x)


val = [23, 345, 4565342, 345, 34562456, 345, 435435, 34545, 345435, 345]
# print(list(filter(f, val)))



print({x for x in range(1, 21) if x %2==0})

def ff(valu):
    return valu %2 == 0

print(list(filter(ff, range(1,21))))

print(list(filter(lambda valu: valu % 2 == 0 , range(1,21))))