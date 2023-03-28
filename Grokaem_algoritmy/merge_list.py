#  coding: utf-8

def sort_merge_lists(list1, list2):
    i = j = 0
    sorted_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1
    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1
    return sorted_list


if __name__ == '__main__':
    # list1, list2 = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(*sort_merge_lists(list1, list2))
