# ID in contest 84059367

# A. Поиск в сломанном массиве

def broken_search(arr, value) -> int:
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == value:
            return mid

        if arr[lo] <= arr[mid]:
            if arr[lo] <= value <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[mid] <= value <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 101) == 3
