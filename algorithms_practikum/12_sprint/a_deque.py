#  ID in context 83540501
class OverflowErrorException(Exception):
    pass


class IndexErrorException(Exception):
    pass


class Deka:
    def __init__(self, __max_n):
        self.__elements = [None] * __max_n
        self.__max_n = __max_n
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def position(self, actual, direction):
        return (actual + direction) % self.__max_n


    def is_empty(self):
        return self.__size == 0

    def push_back(self, item):
        if self.__size != self.__max_n:
            self.__elements[self.__tail] = item
            self.__tail = self.position(self.__tail, +1)
            self.__size += 1
        else:
            raise OverflowErrorException

    def push_front(self, item):
        if self.__size != self.__max_n:
            self.__elements[self.__head - 1] = item
            self.__head = self.position(self.__head, -1)
            self.__size += 1
        else:
            raise OverflowErrorException

    def pop_back(self):
        if self.is_empty():
            raise IndexErrorException
        item = self.__elements[self.__tail - 1]
        self.__elements[self.__tail - 1] = None
        self.__tail = self.position(self.__tail, -1)
        self.__size -= 1
        return item

    def pop_front(self):
        if self.is_empty():
            raise IndexErrorException
        item = self.__elements[self.__head]
        self.__elements[self.__head] = None
        self.__head = self.position(self.__head, +1)
        self.__size -= 1
        return item


def main():
    count_command = int(input())
    deque_size = int(input())

    deque = Deka(deque_size)
    for i in range(count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                result = getattr(deque, operation)(int(*value))
                if result is not None:
                    print(result)
            except OverflowErrorException:
                print('error')
        else:
            try:
                result = getattr(deque, operation)()
                print(result)
            except IndexErrorException:
                print('error')


if __name__ == '__main__':
    main()
