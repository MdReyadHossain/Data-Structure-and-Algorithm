from list import List
from node import Node


class CircularQueue(List):
    def __init__(self, size):
        super().__init__(None, size)

    def enqueue(self, data: int | str):
        newNode: Node = Node(data, None)
        if self.isEmptyList():
            self.head = newNode
            self.tail = newNode
            return data
        newNode.next = self.head
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1
        return data

    def dequeue(self):
        if self.isEmptyList():
            return 'Queue is empty'
        data = self.head.data
        self.head = self.head.next
        self.tail.next = self.head
        return data

    def peek(self):
        if self.isEmptyList():
            return 'Queue is empty'
        return self.head.data

    def printQueue(self):
        print()
