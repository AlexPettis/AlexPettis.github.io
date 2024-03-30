import math


def left(a, b, n):
    # inputs:
    # interval (a,b)
    # number of subintervals n
    # externally defined function f(x)
    # Will calculate left Riemann sum

    h = (b - a) / n
    sum = 0

    for i in range(0, n):
        x = a + i * h
        sum = sum + f(x)

    sum = h * sum
    print(sum)


def f(x):
    return 3 * x + 10
    return math.exp(-3 * x**2)
    return math.sin(x) / x


left(0, 10, 1000)


def right(a, b, n):
    # inputs:
    # interval (a,b)
    # number of subintervals n
    # externally defined function f(x)
    # Will calculate right Riemann sum

    h = (b - a) / n
    sum = 0

    for i in range(1, n + 1):
        x = a + i * h
        sum = sum + f(x)

    sum = h * sum
    print(sum)


right(0, 10, 1000)


def trapezoid(a, b, n):
    # inputs:
    # interval (a,b)
    # number of subintervals n
    # externally defined function f(x)
    # Will calculate trapezoid Riemann sum

    h = (b - a) / n
    sum = (1 / 2) * (f(a) + f(b))

    for i in range(1, n):
        x = a + i * h
        sum = sum + f(x)

    sum = (sum) * h
    print(sum)


trapezoid(0, 10, 1000)
