# просуммировать массив

ar = [2,4,6]

# простым циклом
def summ(a):
    total = 0
    for i in a:
        total += i
    return total

# рекурсивно
def rec_sum(b):
    if not b:
        return 0
    else:
        return b[0] + rec_sum(b[1:])



if __name__ == '__main__':
    print(summ(ar))
    print(rec_sum(ar))