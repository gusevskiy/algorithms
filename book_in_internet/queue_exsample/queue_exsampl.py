class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        #  проверяет очередь на пустоту.
        return self.items == []

    def enqueue(self, item):
        #  добавляет новый элемент в конец очереди.
        self.items.insert(0,item)

    def dequeue(self):
        #  удаляет из очереди передний элемент.
        return self.items.pop()

    def size(self):
        #  возвращает количество элементов в очереди
        return len(self.items)


