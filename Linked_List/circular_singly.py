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

    def insertAt(self, data, index):
        if index == 1:
            self.inserAtFirst(data)
        elif index > 0 and index <= self.size + 1:
            newNode: Node = Node(data)
            currentPtr: Node = self.head
            cnt: int = 1
            while cnt < index - 1:
                currentPtr = currentPtr.next
                cnt += 1
            newNode.next = currentPtr.next
            currentPtr.next = newNode
            self.size += 1
        else:
            self.outOfBound(index)

    def insertAtLast(self, data):
        newNode: Node = Node(data)
        if self.head:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.inserAtFirst(data)

    def removeAtFirst(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.head:
            self.tail.next = self.head.next
            self.head = self.head.next
        self.size -= 1

    def removeAt(self, index):
        currentPtr: Node = self.head
        cnt: int = 1
        while cnt < index - 1:
            currentPtr = currentPtr.next
            cnt += 1
        

    def removeAtLast(self):
        if self.size == 1:
            self.removeAtFirst()
        elif self.head:
            currentPtr: Node = self.head
            cnt: int = 1
            while currentPtr.next != self.tail:
                currentPtr = currentPtr.next
            self.tail = currentPtr
            currentPtr.next = self.head
            self.size -= 1

    def printList(self):
        if self.head:
            currentPtr: Node = self.head
            print('Head -> ', end='')
            while currentPtr.next != self.head:
                print(currentPtr.data, '-> ', end='')
                currentPtr = currentPtr.next
            print(self.tail.data, '(Tail) -> (Head)',
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
