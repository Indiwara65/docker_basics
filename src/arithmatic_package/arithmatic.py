def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
