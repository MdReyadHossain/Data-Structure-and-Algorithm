from list import List
from node import Node


class CircularSinglyList(List):
    def __init__(self):
        super().__init__(None, 0)
        self.tail = None

    def inserAtFirst(self, data):
        newNode: Node = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        else:
            self.head = newNode
            newNode.next = self.head
            self.tail = newNode
        self.size += 1

    def insertAtLast(self, data):
        newNode: Node = Node(data)
        if self.head:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.inserAtFirst(data)

    def printList(self):
        if self.head:
            currentPtr: Node = self.head
            print('Head -> ', end='')
            while currentPtr.next != self.head:
                print(currentPtr.data, '-> ', end='')
                currentPtr = currentPtr.next
            print(currentPtr.data, '(Tail) -> (Head)',
                  currentPtr.next.data, '...')
            print('List Size:', self.size)

        else:
            print('Empty List!')

    def getNextNode(self, index):
        if index > 0 and self.head:
            currentPtr: Node = self.head
            cnt: int = 1
            while cnt < index:
                currentPtr = currentPtr.next
                cnt += 1
            print(currentPtr.data, '->', currentPtr.next.data)

        else:
            self.outOfBound(index)
