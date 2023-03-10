
ar = [1, 4, 7, 12, 5]


# def sum_O(list):
#     Ob = 0
#     List = []
#     for i in list:
#         List.append(i)
#         Ob += 1
#     List[0] *= 2
#     Ob += 1
#     print(List)
#     print('\n', "Ob =", Ob)


def multiplication(array):
    Ob = 0
    mul = []
    indeX = 0
    for a in array:
        a *= array[indeX]
        mul.append(a)
        Ob += 1
    mul.append('\n')
    indeX += 1
    Ob += 1
    return mul








if __name__ == '__main__':
    # sum_O(ar)
    print()
    print(*multiplication(ar))