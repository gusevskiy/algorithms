def BSinBroken (arr, value):
    lo = 0
    hi = len(arr)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == value:
            return mid

        if arr[lo] <= arr[mid]: #сортирован левый
            if arr[lo] <= value <= arr[mid]:
                hi = mid - 1   #ищем в нём
            else:
                lo = mid + 1   #ищем в правом
        else:
            if arr[mid] <= value <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == '__main__':
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    print(BSinBroken(arr, 5))



# def test():
#     arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
#     assert broken_search(arr, 5) == 6


# '''
# print(timeit.timeit(code))