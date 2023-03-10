

# Создать стек на python можно несколькими способами

'''
list_stack = []

list_stack.append('a')
list_stack.append('b')
list_stack.append('c')

print(list_stack)

print(list_stack.pop())

print(list_stack)
'''

'''
from collections import deque


deque_stack = deque()

deque_stack.append('a')
deque_stack.append('b')
deque_stack.append('c')

print(deque_stack)

deque_stack.pop()

print(deque_stack)
'''

'''
from queue_exsample import LifoQueue


my_stack = LifoQueue(maxsize=5)

print(my_stack.qsize())


my_stack.put('a')
my_stack.put('b')
my_stack.put('c')


print('Stack_exsample is Full', my_stack.full())
print('Stack_exsample of Stack_exsample', my_stack.qsize())

print(my_stack.get())
print(my_stack.get())
print(my_stack.get())


print(my_stack.empty())
print(my_stack.qsize())
'''


class Stack:
    def __init__(self):
    	#  в качестве стека взят массив
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


def revstring(mystr):
    """Переворачивает строку с помощью стека"""
    s = Stack()
    for i in mystr:
        s.push(i)
    revers = []
    while s.size() != 0:
        revers.append(s.pop())
    return ''.join(revers)


def parChecker(symbolString):
    """Скобочная последовательность с одним типом скобок"""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        #  усли скобка ')' то из стека выталкивается открывающая скобка
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def parChecker_2(symbolString):
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
    # print(parChecker('((()))'))
    print(parChecker_2('(([()]}))'))
