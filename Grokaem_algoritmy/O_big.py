# О большое - подсчитывает количество операций
from random import randint

# create array
array = []
while len(array) < 10:
    array.append(randint(1, 10))
print('Массив-', *array)

'''
# Вывод значения каждого элемента массива
def output_big_O(array):
    big_O = 0
    for i in array:
        print('элемент ', i)
        big_O += 1
    return big_O


print('кол-во операций вывода ', output_big_O(array))


# Удвоение значения каждого элемента массива
def doubling(array):
    big_O = 0
    arr = []
    for i in array:
        big_O += 1
        arr.append(i * 2)

    return arr


print('удвоеный список ', doubling(array))


# Удвоение значения только первого элемента массива
def doubling_first(array):
    array[0] = array[0] * 2
    return array


print('удвоение первого ', doubling_first(array))
'''


# Создание таблицы умножения для всех элементов массива
# на каждый элемент по очереди
def multiplication(array):
    mul = []
    indeX = 0
    for i in array:
        for a in array:
            a *= array[indeX]
            mul.append(a)
        mul.append('\n')
        indeX += 1
    return mul


print('Умножение')
print(*multiplication(array))
