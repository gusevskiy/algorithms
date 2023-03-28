#  Этот вариант для решений из тестов

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


class Stack:
    def __init__(self):
        #  в качестве стека взят массив.
        self.__items = []

    def is_empty(self):
        #  проверяет стек на пустоту.
        return self.__items == 0

    def push(self, item):
        #  добавляет новый элемент на вершину стека.
        self.__items.append(item)

    def pop(self):
        #  удаляет верхний элемент из стека и вызывает его.
        if not self.is_empty:
            raise IndexError('steck empty')
        return self.__items.pop()

    def peek(self):
        #  возвращает верхний элемент стека, но не удаляет его.
        return self.__items[len(self.__items) - 1]

    def size(self):
        #  возвращает количество элементов в стеке.
        return len(self.__items)


if __name__ == '__main__':
    st = Stack()
    with open(
        '12_sprint/b_reverse_polish_notation copy.txt', 'r'
    ) as f:
        numbers = f.read().split()
    for i in numbers:
        if i in OPERATORS:
            elem_1, elem_2 = st.pop(), st.pop()
            st.push(int(OPERATORS[i](elem_2, elem_1)))
        else:
            st.push(int(i))
    
    print(st.size())
    print(int(st.peek()))
