def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        return 'invalid denominator'
    else:
        return x / y


def multiply(x, y):
    return x * y


def square(x):
    return x**2


def power(x, y):
    return x**y


def sqrt(x):
    x**(1/2)
