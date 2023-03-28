def search_left_humber(seq, x):
    """
    Находит самое левое вхождение числа.
    """
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans


def search_right_number(seq, x):
    """
    Находит самое правое вхождение числа.
    """
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans


def max_number(seq, x):
    """
    Находит Максимальное число
    В закомментированном коде второй вариант
    """
    # ans = seq[0]
    ans = 0
    for i in range(1, len(seq)):  # один (1) экономит на первом проходе
        # if seq(i) > ans:
        if seq(i) > seq[ans]:
            ans = seq[i]
    # return ans
    return seq[ans]


def two_max_number(seq):
    """Находит первый по виличене максимум и втрой за ним"""
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return (max1, max2)


def min_even_numbers(seq):
    """
    Находит минимальное четное числов последовательности
    если его нет выводит -1
    """
    flag = False
    ans = -1
    for i in range(len(seq)):
        # if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
        if seq[i] % 2 == 0 and (not flag or seq[i] < ans):  # вариант с bool
            # переменной, такой код более универсальный
            flag = True
            ans = seq[i]

    return ans


def shortword(words):
    """Найти dct самые короткие слова"""
    minlen = len(words[0])
    for word in words:  # проходимся находим минимальное слово
        if len(word) < minlen:
            minlen = len(word)
    ans = []
    for word in words:  # проходимся еще раз если длина слова = мин.
        # добавляем все такие слова в список
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)


def isleFlood(h):
    """Глубина ям"""
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = i
    ans = 0
    nowm = 0
    for i in range(maxpos):
        if h[i] > nowm:
            nowm = h[i]
        ans += nowm - h[i]
    nowm = 0
    for i in range(len(h) - 1, maxpos, -1):
        if h[i] > nowm:
            nowm = h[i]
        ans += nowm - h[i]
    return ans


def easypeasy(s):
    """Выводит по одному(сокращает) все повторяющие элементы"""
    lastsym = s[0]
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(lastsym)
            lastsym = s[i]
    ans.append((lastsym))
    return ' '.join(ans)


def rle(s):
    """
    Сокращает повторяющиеся элементы до одного и выводит количество их
    повторений
    """
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[0]
    lastpos = 0
    ans = []
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append((pack(lastsym, i - lastpos)))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ' '.join(ans)


if __name__ == '__main__':
    seq = 1, 4, 2, 22, 4, 55
    words = 'asd', 'sd', 'erty', 'er', 'r', 't'
    s = 'AAAAADDDDDDDDGGGGGGTTYKKKKKAAAA'
    # print(search_left_humber(seq, 2))
    # print(search_right_number(seq, 4))
    # print(max(seq))
    # print(two_max_number(seq))
    # print(shortword(words))
    print(easypeasy(s))
    # print(rle(s))