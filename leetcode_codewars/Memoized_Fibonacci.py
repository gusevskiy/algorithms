'''
Преобразуйте функцию в рекурсивную функцию Фибоначчи,
которая с помощью мемоизированной структуры данных позволяет избежать
недостатков древовидной рекурсии. Можете ли вы сделать так, чтобы кеш
мемоизации был приватным для этой функции?
'''


from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# еще решения
memo = {}

def fibonacci_1(n):
    if n in [0, 1]:
        return n
    if n not in memo:
        memo[n] = fibonacci_1(n - 1) + fibonacci_1(n - 2)
    return memo[n]


# еще решения
from functools import cache

@cache
def fibonacci_2(n):
    return n if n in (0, 1) else fibonacci_2(n - 1) + fibonacci_2(n - 2)


if __name__ == '__main__':
    print(fibonacci_1(30))