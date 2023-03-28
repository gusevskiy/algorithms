def bubble_sort(number, array):
    cycle = True
    while cycle:
        cycle = False
        for i in range(len(array)-1):

            if int(array[i]) > int(array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                cycle = True


        if cycle:
            for x in array:
                print(x, end=' ')
            print('')
            cycle = False

if __name__ == '__main__':
    number = int(input())
    array = input().split(' ')
    bubble_sort(number, array)