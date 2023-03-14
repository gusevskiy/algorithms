from random import randint
from time import sleep


arr = [] # Создаем массив
while len(arr) < 10:
    arr.append(randint(1, 10))
print('Массив-', *arr)
print('Сумма по ф-и sum-', sum(arr)) # для проверки

# код для ф-ии сумма.
def fun_sum():
    total = 0
    for i in arr:
        total += i
    return total
print('Сумма по fun_sum-', fun_sum())



# найти наибольший элемент в массиве
def max_number_arr(arr):
    max_num = arr[0]
    index_num = 0
    for i in range(1, len(arr)): # долг сооброжал почему так, но подругому никак
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num
print('Наибольшее число в arr = ', max_number_arr(arr))


# Сортировка массива
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr [1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print('быстрая сортировка массива ', quicksort(arr))

