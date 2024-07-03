from list import List
from node import Node


class CircularQueue(List):
    def __init__(self):
        super().__init__()

    def enqueue(self, data: int | str):
        newNode: Node = Node(data, None)
        if self.isEmptyList():
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return data

    def dequeue(self):
        if self.isEmptyList():
            return "Queue is empty"
        data: int | str = self.head.data
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return data
        self.head = self.head.next
        self.tail.next = self.head
        self.size -= 1
        return data

    def peek(self):
        if self.isEmptyList():
            return "Queue is empty"
        return self.head.data

    def printQueue(self):
        if self.isEmptyList():
            return "Queue is empty"
        currentPtr: Node = self.head
        sl: int = 1
        print('Queue:')
        while currentPtr:
            print(f'\t{sl}.', currentPtr.data)
            if currentPtr == self.tail:
                break
            currentPtr = currentPtr.next
            sl += 1
