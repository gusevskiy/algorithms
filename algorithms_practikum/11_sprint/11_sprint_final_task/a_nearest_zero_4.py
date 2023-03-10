# ID in context 82764784


from typing import List, Tuple


def zerros(count, street):

    forvard_street = []
    back_street = []
    zerro = []
    for_index = 1
    bac_index = 1
    result = []

    for i, y in enumerate(street):
        if y == 0:
            forvard_street.append(0)
            zerro.append(i)
            for_index = 1
        elif y >= 1:
            forvard_street.append(for_index)
            for_index += 1

    for i, y in enumerate(street[::-1]):
        if y == 0:
            back_street.append(0)
            bac_index = 1
        elif y >= 1:
            back_street.append(bac_index)
            bac_index += 1

    slice_for = forvard_street[zerro[0]:zerro[-1]]
    slice_bac = list(reversed(back_street))[zerro[0]:zerro[-1]+1]

    for i in range(len(slice_for)):
        result.append(min(slice_for[i], slice_bac[i]))

    return (
        list(
            reversed(back_street)
        )[:zerro[0]]+result+forvard_street[zerro[-1]:]
    )


def read_input() -> Tuple[int, List[int]]:
    length = int(input())
    number_street = [int(num) for num in input().split(' ')]
    return length, number_street


if __name__ == '__main__':
    street = [6,10,13,31,35,39,0,59,66,68,73,74,0,87,89,96,99]
    # street = 99, 0, 100, 72, 43, 49, 0, 51, 19, 61, 93, 31
    # for i in street[2:5]:
    #     print(i)
    # print(long_street(8, street))
    print(' '.join([str(x) for x in zerros(16, street)]))


    # length, number_street = read_input()
    # print(*zerros(length, number_street))
