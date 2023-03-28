# Алгоритм Быстрой сортировки Хоара
import random

# Как нибудь попробавать переделать на словарь

def sort_hoara(array):
    if len(array) < 2:  # базовый случай,
        return array    # массивы с 0 или 1 элементами фактически отсортированы
    casually = array[random.randint(0, len(array)-1)]
    left = [u for u in array if u < casually]
    center = [u for u in array if u == casually]
    right = [u for u in array if u > casually]
    return sort_hoara(left) + center + sort_hoara(right)


# if __name__ == '__main__':
#     number = int(input())
#     competitors = [transformation(input().split()) for _ in range(number)]
#     left = 0
#     quick_sort(competitors, left, len(competitors))
#     print(*(list(zip(*competitors))[2]), sep="\n")


if __name__ == '__main__':
    # number = int(input())
    play_keys = ['name', 'task', 'fine']
    players = []
    with open('reshbrtbt.txt', 'r') as f:
        data = f.readlines()
    for i in data:
        players.append(dict(zip(play_keys, i.split())))
    print(players)
    print(sort_hoara(players, key=lambda x: x['task']))