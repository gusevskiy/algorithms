#  ID in context 83540682


OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == 0

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty:
            raise IndexError('steck empty')
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def size(self):
        return len(self.__items)


def solution(numbers):
    st = Stack()
    for i in numbers:
        if i in OPERATORS:
            elem_1, elem_2 = st.pop(), st.pop()
            st.push(int(OPERATORS[i](elem_2, elem_1)))
        else:
            st.push(int(i))
    return int(st.peek())


if __name__ == '__main__':
    inp_string = input().split()
    print(solution(inp_string))
