def print_hello(n):
    if n <= 0:
        pass
    else:
        print("Hello")
        print_hello(n - 1)


# print_hello(5)

def print_int(n):
    if n <= 0:
        return None
    else:
        print(n)
        print_int(n-1)
        print(n)

print_int(3)


