def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    return a * (x * x) + b * x + c


if __name__ == '__main__':
    print(evaluate_function(-8, -5, -2, 7))
