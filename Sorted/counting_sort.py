def counting_sort(array):
    counted_values = [0] * 12
    for value in array:
        counted_values[value] += 1

    dat = []
    index = 0
    for value in range(12):
        for i in range(counted_values[value]):
            array[index] = value
            index += 1



if __name__ == '__main__':
    nums = [5, 7, 1, 0, 1, 5, 11, 1]
    print(counting_sort(nums))
