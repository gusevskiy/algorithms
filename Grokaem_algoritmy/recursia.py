from random import randint

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x -1)


# for i in range(10):
#     print(i)

'''
# рекурсивная ф-я
def recurs_sum(ar):
    if not ar:
        return 0
    return ar[0] + recurs_sum(ar[1:])
print('Сумма по recurs_sum-', recurs_sum(ar))
'''

# Найти наибольший элемент в списке
# a = 0
# for i in ar:
#     if i > a:
#         a = i
# print(a)


if __name__ == '__main__':
    print(fact(5))