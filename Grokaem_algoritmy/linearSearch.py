array_1 = [1, 4, 4, 6, 7, 8, 3, 1, 34, 65, 9]

def linear_search(array: list[int], numb: int) -> str:
    BigO = 0
    for i in array:
        BigO += 1
        if array[i] == numb:
            return f'{i}, number of cycles = {BigO}'
    return None


    # List Comprehension
    # new_list = [i for i in array if i == numb]
    # return array.index(*new_list)


print(f'index numb in array_1 =', linear_search(array_1, 3))
