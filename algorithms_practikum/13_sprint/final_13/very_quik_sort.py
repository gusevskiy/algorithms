# ID in contest 84110300

# B. Эффективная быстрая сортировка
# Алгоритм Быстрой сортировки Хоара
import random


def sort_hoara(array):
    array = array
    if len(array) < 2:  # базовый случай,
        return array    # массивы с 0 или 1 элементами фактически отсортированы
    casually = array[random.randint(0, len(array)-1)]
    left = [u for u in array if u < casually]
    center = [u for u in array if u == casually]
    right = [u for u in array if u > casually]
    return sort_hoara(left) + center + sort_hoara(right)


def swap_places(data):
    return [-int(data[1]), int(data[2]), data[0]]


if __name__ == '__main__':
    number = int(input())
    players = [swap_places(input().split()) for _ in range(number)]
    result = sort_hoara(players)
    for i in result:
        print(i[2])





















    # number = int(input())
    # play_keys = ['name', 'task', 'fine']
    # players = []
    # with open('very_quik_sort.txt', 'r') as f:
    #     data = f.readlines()
    # for i in data[::-1]:
    #     players.append(
    #         [-int(i.split()[1]), int(i.split()[2]), i.split()[0]]
    #     )
    # print(players)
    # print(sort_hoara(players))
# def quicksort(data):
#     for i in data:
#         # players.append(dict(zip([x for x in range(len(i.split()))], i.split(
#         players.append(dict(zip(play_keys, i.split())))
#
#     a = sorted(
#         players, key=lambda x: (x['task'], x['name']), reverse=True
#     )
#
#     for i in a:
#         print(i['name'])