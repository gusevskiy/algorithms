class Deka:
    def __init__(self, max_n):
        self.queue = [None] * max_n
        self.max_n = max_n
        self.head = 0
        self.tail = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push_back(self, item):
        #  добавить элемент в конец дека.
        if self.size != self.max_n:  # если дека не заполнена полностью
            self.queue[self.tail] = item  # то последний индекс = item
            self.tail = (self.tail + 1) % self.max_n  # для обнуления
            self.size += 1  # ну и размер соответственно увеличивается
        else:
            raise OverflowError

    def push_front(self, item):
        #  добавить элемент в начало дека.
        if self.size != self.max_n:  # если дека не заполнена полностью
            self.queue[self.head - 1] = item
            self.head = (self.head - 1) % self.max_n
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self):
        #  вывести последний элемент дека и удалить его.
        if self.isEmpty():
            raise MemoryError
        item = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return item

    def pop_front(self):
        #  вывести первый элемент дека и удалить его.
        if self.isEmpty():
            raise MemoryError
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return item


def main():
    count_command = int(input())
    queue_size = int(input())

    queue = Deka(queue_size)
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
            except MemoryError:
                print('error')
        else:
            try:
                result = commands[operation]()
                print(result)
            except MemoryError:
                print('error')


if __name__ == '__main__':
    main()
