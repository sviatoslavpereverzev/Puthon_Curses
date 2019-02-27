"""
sum (5)= 1+2+3+4+5
"""

def summ(n):
    if n <= 1:
        return 1
    else:
        return n+summ(n-1)

"""
factorial(5)= 1+2+3+4+5
"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)



print(factorial(998))