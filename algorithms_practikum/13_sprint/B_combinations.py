
SYMBOLS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def combination(a, b, s=''):
    if a == b:
        print(s)
    else:
        combination(a[0] + b[0], b[0+1])


print(combination('abc', 'def'))




# if __name__ == '__main__':
#     numbers = list(map(int, '23'))
#     count = len(SYMBOLS[numbers[0]]) * len(SYMBOLS[numbers[1]])
#
#     print(count)
#
# print(len(SYMBOLS[3]))
