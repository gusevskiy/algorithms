
# num_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#            11, 12, 13, 14, 15, 16, 17, 18, 19,
#            20, 21, 22, 23, 24, 25, 26, 27, 28,
#            29, 30, 31, 32, 33, 34, 35, 36, 37,
#            38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
#
# offset_arr = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
#               20, 21, 22, 23, 24, 25, 26, 27, 28,
#               29, 30, 31, 32, 33, 34, 35, 36, 37,
#               38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
#               0, 1, 2, 3, 4, 5, 6, 7, 8]



# create_num_arr = list(range(50))
# print(num_arr)

# Перебором поиск наименьшего элемента в массиве стр 57
def find_smalles(ar):
    smalles = ar[0]
    smalles_index = 0
    for i in range(1, len(ar)):
        if ar[i] < smalles: # для максимального нужно поменять знак >
            smalles = ar[i]
            smalles_index = i
    # return 'index min numbers = ', smalles_index, 'smalles =', smalles
    return smalles_index


# сортировка выбором => работает
def selctionSort(ar):
    new_arr = []
    for i in range(len(ar)):
        smalles = find_smalles(ar)
        new_arr.append(ar.pop(smalles))
    return new_arr





if __name__ == '__main__':
    # print(find_smalles([5, 3, 6, 2, 10]))

    print(selctionSort([5, 3, 6, 2, 10]))