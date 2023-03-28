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
    
    def __get_index(self, method):
        if method == 'push_front':
            return (self.__head - 1) % self.__max_n
        if method == 'push_back':
            return (self.__tail + 1) % self.__max_n
        if method == 'pop_front':
            return (self.__head + 1) % self.__max_n
        if method == 'pop_back':
            return (self.__tail - 1) % self.__max_n


    def is_full(self):
        return self.__size == self.__max_n

    def is_empty(self):
        return self.__size == 0

    def push_back(self, item):
        if self.is_full:
            raise OverflowErrorException
        else:
            self.__elements[self.__tail] = item
            self.__tail = self.__get_index('push_back')
            self.__size += 1
            

    def push_front(self, item):
        if self.is_full:
            raise OverflowErrorException
        else:
            self.__elements[self.__head - 1] = item
            self.__head = self.__get_index('push_front')
            self.__size += 1

    def pop_back(self):
        if self.is_empty:
            raise IndexErrorException
        item = self.__elements[self.__tail - 1]
        self.__elements[self.__tail - 1] = None
        self.__tail = self.__get_index('pop_back')
        self.__size -= 1
        return item

    def pop_front(self):
        item = self.__elements[self.__head]
        self.__elements[self.__head] = None
        self.__head = self.__get_index('pop_front')
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
            except OverflowError:
                print('error')
        else:
            try:
                result = getattr(deque, operation)()
                print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()