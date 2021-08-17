def print_fibonacci(n):
    """This function prints
    Fibonacci series upto n
    """
    a, b = 0, 1

    while a <= n:
        print(a)
        a, b = b, a + b


print(print_fibonacci.__doc__)

print_fibonacci(100)