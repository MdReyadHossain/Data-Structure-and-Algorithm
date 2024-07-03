from node import Node
from list import List

# LIFO -> Last In First Out


class Stack(List):
    def __init__(self) -> None:
        super().__init__(None, 0)

    def push(self, data: int):
        newNode: Node = Node(data)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        if self.isEmptyList():
            return "Stack is empty"
        self.head = self.head.next
        self.size -= 1

    def peek(self):
        if self.isEmptyList():
            return "Stack is empty"
        return self.head.data

    def printStack(self):
        if self.isEmptyList():
            return "Stack is empty"
        currentPtr: Node = self.head
        sl: int = self.size
        print('Stack: ')
        while currentPtr.next:
            print(f'\t{sl}.', currentPtr.data)
            sl -= 1
            currentPtr = currentPtr.next
        print(f'\t{sl}.', currentPtr.data, '\n')
