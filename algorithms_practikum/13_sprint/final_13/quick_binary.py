#  быстрая сортировка и бинарный поиск, но
#  индекс элемнта находит неправельно нужно
#  индекс выводить из не отсортированого массива

def qquicksort(ar):
    if len(ar) < 2:
        return ar
    else:
        pivot = ar[0]
        less = [i for i in ar[1:] if i <= pivot]
        greater = [i for i in ar[1:] if i > pivot]
        return qquicksort(less) + [pivot] + qquicksort(greater)


def broken_search(ar, item) -> int:
    ar = qquicksort(ar)
    low = 0
    high = len(ar)-1
    while low <= high:
        mid = (low + high) // 2
        gees = ar[mid]
        if gees == item:
            return mid
        if gees > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    print(broken_search(arr, 5))
