class Stack:
    def __init__(self):
        #  в качестве стека взят массив.
        self.items = []

    def isEmpty(self):
        #  проверяет стек на пустоту.
        return self.items == []

    def push(self, item):
        #  добавляет новый элемент на вершину стека.
        self.items.append(item)

    def pop(self):
        #  удаляет верхний элемент из стека и вызывает его.
        return self.items.pop()

    def peek(self):
        #  возвращает верхний элемент стека, но не удаляет его.
        return self.items[len(self.items) - 1]

    def size(self):
        #  возвращает количество элементов в стеке.
        return len(self.items)


def is_correct_bracket_seq(symbolString):
    """Скобочная последовательность с разными типоми скобок"""
    s = Stack()
    bracket = {'(': ')', '{': '}', '[': ']'}
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in bracket.keys():
            s.push(symbol)
        elif not s.isEmpty() and bracket[s.peek()] == symbol:
            s.pop()
        else:
            balanced = False
            break

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    symbolString = '({})({[]}[])'
    print(is_correct_bracket_seq(symbolString))
