from node import Node


class Stack:
    def __init__(self) -> None:
        self.head: Node = None
        self.size = 0

    def emptyList(self):
        print('Empty List!')
        return self.head == None

    def push(self, data: int):
        newNode: Node = Node(data)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1
        else:
            self.emptyList()

    def peek(self):
        if self.head:
            return self.head.data
        else:
            self.emptyList()

    def printStack(self):
        currentPtr: Node = self.head
        print('Stack: ')
        while currentPtr.next:
            print(currentPtr.data)
            currentPtr = currentPtr.next
        print(currentPtr.data, '\n')
