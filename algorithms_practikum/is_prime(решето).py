# поиск простых чисел

def is_prime_1(n):
    """Сложность On"""
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def is_prime_2(n):
    """O корень n"""
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def get_smaller_primes(n):
    smaller_primes = []
    for num in range(2, n + 1):
        if is_prime_1(num):
            smaller_primes.append(num)
    return smaller_primes


def eratosthenes(n):
    # O(nlog(logn)).
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(2 * num, n + 1, num):
                numbers[j] = False
    return numbers


def get_least_primes_linear(n):
    """Решето Эратосфера"""
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


if __name__ == '__main__':
    # print(eratosthenes(15))
    print(get_least_primes_linear(8))
