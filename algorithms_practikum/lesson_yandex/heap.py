
def puch_heap(head_list, x):
    head_list.append(x)
    pos = len(head_list) - 1
    while pos > 0 and head_list[pos] > head_list[pos // 2]:
        # смена элементав местоми (своп)
        head_list[pos], head_list[pos // 2] = head_list[pos // 2], head_list[pos]
        pos = pos // 2