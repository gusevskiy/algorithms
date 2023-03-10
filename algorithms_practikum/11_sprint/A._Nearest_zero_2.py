from typing import List, Tuple


def long_street(total, list_count):
    dubl_list = [0] * total
    zero_index = '0'
    zeros = []
    for i, x in enumerate(list_count):
        if x == zero_index:
            zeros.append(i)
    print(zeros)


def zerros(total, list_count):
    zero_index = []
    index_back = []
    index = []
    ds = []
    a = 1
    for i, y in enumerate(list_count):
        if y == 0:
            index.append(0)
            zero_index.append(i)
            a = 1
        elif y >= 1:
            index.append(a)
            a += 1
    if len(zero_index) == 1:
        for e, r in enumerate(list_count[:zero_index[-1]+1][::-1]):
            if r == 0:
                index_back.append(e)
                a = 1
            elif r >= 1:
                index_back.append(a)
                a += 1
        index_back_revers = list(
                reversed(index_back)
            ) + index[zero_index[-1] + 1:]
        return index_back_revers

    if len(zero_index) > 1:
        for e, r in enumerate(list_count[:zero_index[-1]+1][::-1]):
            if r == 0:
                index_back.append(e)
                a = 1
            elif r >= 1:
                index_back.append(a)
                a += 1
    index_back_revers = list(reversed(index_back))+index[zero_index[-1]+1:]
    for i in range(len(list_count)):
        ds.append(min(index_back_revers[i], index[i]))
    return ds


if __name__ == '__main__':
    street = 10,13,31,35,39,0,0,59,0,66,68,73,74,0,0,0,87,89,96,99
    # street = 99, 0, 100, 72, 43, 49, 0, 51, 19, 61, 93, 31
    # for i in street[2:5]:
    #     print(i)
    # print(long_street(8, street))
    print(zerros(8, street))