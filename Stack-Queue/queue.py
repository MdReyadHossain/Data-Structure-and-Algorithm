from list import List
from node import Node

class Queue(List):
    def __init__(self):
        super().__init__(None, 0)

    def enqueue(self, data):
        self.size += 1
        newNode: Node = Node(data, None)
        if self.head:
            self.tail.next = newNode
            self.tail = newNode
            return newNode
        self.head = newNode
        self.tail = newNode

    def dequeue(self):
        if self.head:
            self.size -= 1
            node: Node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return node.data
        self.isEmptyList()

    def printQueue(self):
        currentPtr: Node = self.head
        sl: int = 1
        print('Queue:')
        while currentPtr:
            print(f'\t{sl}.', currentPtr.data)
            sl += 1
            currentPtr = currentPtr.next
        
