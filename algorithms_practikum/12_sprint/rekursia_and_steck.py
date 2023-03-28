def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(3))