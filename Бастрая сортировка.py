from time import sleep

ar = [1, 4, 7, 12, 55]


def sum_arr(ar):
    """сумма массива рекурсивно"""
    if ar ==[]:
        return 0
    else:
        s = ar[0] + sum_arr(ar[1:])
        return s

def max_num_in_list(ar):
    """наибольший элемент массива"""
    if len(ar) == 1:
        return ar[0]
    else:
        max_ = ar[0]
        for i in ar:
            if max_ < i:
                max_ = i
        return max_



    # Сортировка массива
def quicksort(ar):
    if len(ar) < 2:
        return ar
    else:
        pivot = ar[0]
        less = [i for i in ar[1:] if i <= pivot]
        greater = [i for i in ar [1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
#print('быстрая сортировка массива ', quicksort(ar))




def print_import_slip1(list):
    for i in list:
        print(i, end=' ')


def print_import_slip2(list):
    for i in list:
        sleep(2) # задержка 2 секунды
        print(i, end=' ')



if __name__ == '__main__':
    print(quicksort(ar))
    # print_import_slip1(ar)
    # print()
    # print_import_slip2(ar)
    # print(sum_arr(ar))
    # print(ar[1:])
    # print(max_num_in_list(ar))