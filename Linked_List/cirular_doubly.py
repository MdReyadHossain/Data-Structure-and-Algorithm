from list import List
from node import Node


class CircularDoublyList(List):
    def __init__(self):
        super().__init__(None, 0)
        self.tail: Node = None

    def insertAtFirst(self, data):
        newNode: Node = Node(data)
        if self.size == 0:
            self.head = newNode
            newNode.next = self.head
            self.tail = newNode
            self.tail.next = self.head
            self.head.previous = self.tail
        else:
            newNode.next = self.head
            newNode.previous = self.tail
            self.tail.next = newNode
            self.head.previous = newNode
            self.head = newNode

        self.size += 1

    def insertAt(self, data, index):
        newNode: Node = Node(data)
        if index < 1 or index > self.size + 1:
            self.outOfBound(index)
        elif self.size == 0 or index == 1:
            self.insertAtFirst(data)
        else:
            currentPtr: Node = self.head
            cnt: int = 1
            while cnt < index - 1:
                currentPtr = currentPtr.next
                cnt += 1
            nextPtr: Node = currentPtr.next
            if nextPtr != self.head:
                currentPtr.next = newNode
                newNode.previous = currentPtr
                newNode.next = nextPtr
                nextPtr.previous = newNode
            else:
                self.insertAtLast(data)
                return

            self.size += 1

    def insertAtLast(self, data):
        newNode: Node = Node(data)
        if self.size > 0:
            newNode.next = self.head
            newNode.previous = self.tail
            self.head.previous = newNode
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.insertAtFirst(data)

    def removeAtFirst(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.head:
            self.tail.next = self.head.next
            self.head.next.previous = self.tail
            self.head = self.head.next
        self.size -= 1

    def removeAtLast(self):
        self.size -= 1

    def printList(self):
        if self.head:
            currentPtr: Node = self.head
            print('...', currentPtr.previous.data,
                  '(Tail) <-> Head <-> ', end='')
            while currentPtr.next != self.head:
                print(currentPtr.data, '<-> ', end='')
                currentPtr = currentPtr.next
            print(self.tail.data, '(Tail) <-> (Head)',
                  currentPtr.next.data, '...')

            print('...', currentPtr.next.data,
                  '(Head) <-> Tail <-> ', end='')
            while currentPtr.previous != self.tail:
                print(currentPtr.data, '<-> ', end='')
                currentPtr = currentPtr.previous
            print(self.head.data, '(Head) <-> (Tail)',
                  currentPtr.previous.data, '...')

            print('List Size: ', self.size)
        else:
            print('Empty List!\nList Size: ', self.size)
