def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a