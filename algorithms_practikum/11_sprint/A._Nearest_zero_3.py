from typing import List, Tuple


def zerros(count, forward_street) -> List[int]:
    back_street = list(reversed(forward_street))
    result =[]
    forward = []
    back = []

    for i in range(count):
        if forward_street[i] == 0:
            forward.append(i)
        if back_street[i] == 0:
            back.append(i)
    for i in range(count):
        ba = abs(i - back[0])
        fo = abs(i - forward[0])

        if forward_street[i] == 0:
            if len(forward) > 1:
                forward.pop(0)
        if back_street[i] == 0:
            if len(back) > 1:
                back.pop(0)
        forward_street[i] = fo
        back_street[i] = ba
    back_street = back_street[::-1]
    for i in range(count):
        result.append(min(forward_street[i], back_street[i]))

    return result


if __name__ == '__main__':
    street = [6,10,13,31,35,39,0,59,66,68,73,74,0,87,89,96,99]
    # street = 99, 0, 100, 72, 43, 49, 0, 51, 19, 61, 93, 31
    # for i in street[2:5]:
    #     print(i)
    # print(long_street(8, street))
    print(' '.join([str(x) for x in zerros(16, street)]))