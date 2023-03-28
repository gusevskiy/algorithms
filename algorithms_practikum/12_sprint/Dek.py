class Dek:
    def __init__(self, max_size: int):
        self._elements = [None] * max_size
        self._max_size = max_size
        self._head = 0
        self._tail = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push_back(self, value: int):
        if self._size != self._max_size:
            self._elements[self._tail] = value
            self._tail = (self._tail + 1) % self._max_size
            self._size += 1
        else:
            raise OverflowError

    def push_front(self, value: int):
        if self._size != self._max_size:
            self._elements[self._head - 1] = value
            self._head = (self._head - 1) % self._max_size
            self._size += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        x = self._elements[self._tail - 1]
        self._elements[self._tail - 1] = None
        self._tail = (self._tail - 1) % self._max_size
        self._size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self._elements[self._head]
        self._elements[self._head] = None
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return x


def main():
    count_command = int(input())
    queue_size = int(input())

    queue = Dek(queue_size)
    commands = {
        'push_front': queue.push_front,
        'push_back': queue.push_back,
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back,
    }
    for i in range(count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                result = commands[operation](int(*value))
                if result is not None:
                    print(result)
            except OverflowError:
                print('error')
        else:
            try:
                result = commands[operation]()
                print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()