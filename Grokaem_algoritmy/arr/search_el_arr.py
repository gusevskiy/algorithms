offset_arr = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              20, 21, 22, 23, 24, 25, 26, 27, 28,
              29, 30, 31, 32, 33, 34, 35, 36, 37,
              38, 39, 40, 200, 41, 42, 43, 44, 45, 46, 47, 48, 49,
              0, 1, 2, 3, 4, 5, 6, 7, 8]



# перебором поиск максимального элемента в массиве

def large(arr):
    max_ = arr[0]
    o_big = 0
    for ele in arr:
        o_big += 1
        if ele > max_:
           max_ = ele
    return max_, o_big



# линейный алгоритм поиск мин
def min_item(items, *, key=lambda x: x):
    min_, *items = items
    for item in items:
        if key(item) < key(min_):
            min_ = item
    return min_


_sentinel = object()

def min(first, *args, key=lambda x: x, default=_sentinel):
    if not args:  # first is an iterable
        args = iter(first)
        try:
            first = next(args)
        except StopIteration: # empty
            if default is _sentinel:
                raise ValueError("min() arg is an empty sequence") from None
            return default
    elif default is not _sentinel:
        raise TypeError("Cannot specify a default for min() with multiple positional arguments")
    min_key = key(first)
    for arg in args:
        k = key(arg)
        if k < min_key:
            min_key = k
            first = arg
    return first

if __name__ == '__main__':
    # print(large(offset_arr))
    print(find_smalles(offset_arr))
    # print(min_item(offset_arr))
    # print(min(offset_arr))

