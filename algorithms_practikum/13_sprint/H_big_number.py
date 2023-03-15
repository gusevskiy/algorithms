def comparate(num1, num2):
    return num1 < num2


def big(array, less):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        a = int(key_item + array[j])
        b = int(array[j] + key_item)
        f = less(b, a)
        while j >= 0 and f:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
    print(''.join(array))


if __name__ == '__main__':
    number = int(input())
    array = input().split(' ')
    big(array, comparate)


    # array = []
    # with open('big_number.txt', 'r') as f:
    #     data = f.readlines()
    #     for i in data:
    #         array.append(i.strip())
    # print(int(array[0]))
    # print(big(int(array[0]), int(array[1])))

    # a = 344
    # n = int(str(a)[0])
    #
    # print(n)