"""Числа float неточны из-за того, как они представляются в памыти"""
sum = 0
for i in range(10):
    sum = sum + 0.1

print(sum)
