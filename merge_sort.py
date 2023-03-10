def merge_sort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                mylist[k] = left[i]
                i += 1
            else:
                mylist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1
    return mylist



if __name__ == "__main__":
    array = [5, 4, 1, 8, 7, 2, 6, 3]
    print(merge_sort(array))
