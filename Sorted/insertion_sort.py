def insertion_sort(array):
    # for i in range(1, len(array)):
    #     item_to_insert = array[i]
    #     j = i - 1
    #     while j >= 0 and item_to_insert < array[j]:
    #         array[j+1] = array[j]
    #         j -= 1
    #     array[j+1] = item_to_insert
        # print(f'step {j}, sorted {i + 1} element: {array}')

    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
        print(f'step {j}, sorted {i + 1} element: {array}')


if __name__ == '__main__':
    insertion_sort([11, 2, 9, 7, 1])