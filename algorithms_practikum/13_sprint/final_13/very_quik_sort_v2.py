# ID in contest 84267513

from dataclasses import dataclass


@dataclass
class Players:
    __slots__ = ['username', 'task', 'fine']
    username: str
    task: int
    fine: int

    def __str__(self):
        return self.username

    def __lt__(self, other):
        if isinstance(other, Players):
            return (
                    (-self.task, self.fine, self.username) <
                    (-other.task, other.fine, other.username)
            )
        return NotImplemented


def quicksort(array: list, start=0, end=0):
    def _partition(low, high):
        if low >= high:
            return
        left = low
        right = high
        pivot = array[(right + left) // 2]
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _partition(low, right)
        _partition(left, high)

    _partition(start, end - 1)


if __name__ == '__main__':
    number = int(input())
    players = []
    for _ in range(number):
        username, task, fine = input().split()
        players.append(
            Players(task=int(task), fine=int(fine), username=username)
        )
    quicksort(players, end=number)
    print(*players, sep='\n')
