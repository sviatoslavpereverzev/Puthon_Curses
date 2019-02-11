from time import time

print(time())

z = [x for x in range(1000000)]
# print(z)
start = time()
reverse_1 = z
reverse_1.reverse()
end = time()
print('Время первого реверса {}'.format(end -start))

start = time()
reverse_2 = []
for i in range(1000000):
    reverse_2.append(z[-i - 1])
#     print((-i - 1))
# print(reverse_2)
end = time()
print('Время второго реверса {}'.format(end -start))