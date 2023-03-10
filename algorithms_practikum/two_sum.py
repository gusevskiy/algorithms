from datetime import datetime


def time_it(func):
    """calculation of the function operation time"""
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@time_it
def two_sum(number, X):
    for i in range(0, len(number)):
        for j in range(i+1, len(number)):
            if number[i] + number[j] == X:
                return number[i], number[j]
    return None, None


@time_it
def two_sum_with_sort(number, X):
    sort_number = sorted(number)
    left = 0
    right = len(sort_number) - 1
    while left < right:
        current_sum = sort_number[left] + sort_number[right]
        if current_sum == X:
            return sort_number[left], sort_number[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1
    return None, None


@time_it
def two_sum_extra_ds(number, X):
    previous = set()
    for A in number:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)
    return None, None


if __name__ == '__main__':
    a = 2, 1, 3, 5, 5, 2, 1, 3, 5, 5, 2, 1, 3, 5, 5, 2, 1, 3, 5, 5,


    print(two_sum(a, 8))
    print(two_sum_with_sort(a, 8))
    print(two_sum_extra_ds(a, 8))