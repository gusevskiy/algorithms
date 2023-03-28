# Этот код не рабочий


def merge_sort(L):
    if len(L) < 2:
        return L
    else:
        centr = len(L) // 2
        left_L = merge_sort(L[:centr])
        right_L = merge_sort(L[centr:])
        return merge(left_L, right_L)

def merge(left, right):
    result_list = []
    i, j = 0, 0
    a = len(left)
    b = len(right)
    while j < a and i < b:
        u = left[i]
        r = right[j]
        if u < r:
            result_list.append(left[i])
            i += 1
        else:
            result_list.append(right[j])
            j += 1
    if left:
        result_list = result_list + left[i:]
    if right:
        result_list = result_list + right[j:]

    return result_list


if __name__ == '__main__':
    a = [1, 4, 9, 2, 10, 11]
    print(merge_sort(a))
