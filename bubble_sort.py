offset_arr = [90, 11, 40, 167, 19]

# for i in range(len(offset_arr)-1):
#     print(offset_arr[i])
def bubblesort(array):
    length = len(array)
    # count = 0
    # for i in range(length-1):
    #     for x in range(length-1-i):
    #         # если соседний элемент меньше
    #         if array[x+1] < array[x]:
    #             # меняем их местами (можно через множ присваивание a,b=b,a)
    #             temporary = array[x]
    #             array[x] = array[x+1]
    #             array[x+1] = temporary
    #         count += 1
    # return array, count

# тоже самое через while
    i = 0
    while i<(length-1):
        j = 0
        while j<(length-1)-i:
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            j+=1
        i+=1
    return array





print(*bubblesort(offset_arr))