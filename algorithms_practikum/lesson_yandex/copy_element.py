# from ..two_sum import  time_it


def elementy(list):
    ans = ''
    anscnt = 0
    for now in set(list):
        nowcnt = 0
        for j in range(len(list)):
            if now == list[j]:
                nowcnt += 1
        if nowcnt > anscnt:
            ans = now
            anscnt = nowcnt
    return anscnt


def elementy_2(list):
    dct = {}
    anscnt = 0
    for now in list:
        if now not in dct:
            dct[now] = 0
        dct[now] += 1
    for kcg in dct:
        if dct[kcg] > anscnt:
            anscnt = dct[kcg]
    return anscnt


if __name__ == '__main__':
    word = 'a', 'd', 'a', 'd', 'a'
    print(elementy(word))
    print(elementy_2(word))
