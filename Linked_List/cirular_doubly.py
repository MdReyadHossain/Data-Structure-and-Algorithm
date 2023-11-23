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
        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head

    def printList(self):
        currentPtr: Node = self.head
        while currentPtr.next != self.head:
            print()
