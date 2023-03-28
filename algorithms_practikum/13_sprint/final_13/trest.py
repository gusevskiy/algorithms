from dataclasses import dataclass
import random


@dataclass
class Players:
    __slots__ = ['username', 'task', 'fine']
    username: str
    task: int
    fine: int

    def __gt__(self, other):
        if self.fine == other.fine:
            return self.username > other.username
        return self.task < other.task

    # def __lt__(self, other):
    #     return other > self

    def __lt__(self, other):
        if self.task == other.task:
            return self.fine < other.fine


    def __str__(self):
        return self.username


def swap_places(data):
    return [int(data[1]), int(data[2]), data[0]]


def sort_hoara(array):
    if len(array) < 2:
        return array
    casually = array[random.randint(0, len(array) - 1)]
    left = [u for u in array if u < casually]
    center = [u for u in array if u == casually]
    right = [u for u in array if u > casually]
    return sort_hoara(left) + center + sort_hoara(right)


if __name__ == '__main__':

    # number = int(input())
    # data = []
    # for _ in range(number):
    #     username, task, fine = input().split()
    #     data.append(Players(username, int(task), int(fine)))
    # print(*sort_hoara(data), sep='\n')

    a = [Players(username='ma', task=2, fine=100),
         Players(username='mb', task=3, fine=100),
         Players(username='mv', task=4, fine=1),
         Players(username='mg', task=5, fine=100),
         Players(username='vi', task=6, fine=100)]
    #
    # sorted(a, reverse=False)
    #
    print(a.sort())
    # print(a.index().)

'''
[
 Players(username='alla', task=4, fine=100),
 Players(username='gena', task=6, fine=1000),
 Players(username='gosha', task=2, fine=90),
 Players(username='rita', task=2, fine=90),
 Players(username='timofey', task=4, fine=80)
 ]
 
5
me 4 100
ma 6 100
wo 2 1
ri 2 2
ai 4 4
 
'''
