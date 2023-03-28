from math import sqrt


def is_square(n):
    if n < 0:
        return False
    if sqrt(n).is_integer():
        return True
    return False


print(is_square(-1))


# print(sqrt(-1).is_integer())