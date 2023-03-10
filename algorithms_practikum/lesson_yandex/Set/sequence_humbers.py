'''
Дана последовательность положительных чисел длинной N и число X

Нужно найти два различных числа А и В из последовательности,
таких что А + В = X. Или вернуть 0, 0 если такой пары нет
'''


def twotermswithsumx(nums, x):
    """
    перебирается по индексам
    Решение за О(n**2)
    """
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            if nums[a] + nums[b] == x:
                return nums[a], nums[b]
    return 0, 0


def twotermswithsumx_2(nums, x):
    """Решение за О(n)"""
    prevnums = set()
    for nownum in nums:
        if x - nownum in prevnums:
            return nownum, x - nownum
        prevnums.add(nownum)
    return 0, 0


if __name__ == '__main__':
    nums = 1, 3, 5, 8, 2

    print(twotermswithsumx_2(nums, 7))