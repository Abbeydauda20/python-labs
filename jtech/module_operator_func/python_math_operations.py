def add(x: int, y: int):
    return x + y


def sub(x: int, y: int):
    return x - y


def fact(x: int):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def multi(x: int, y: int):
    return x * y
