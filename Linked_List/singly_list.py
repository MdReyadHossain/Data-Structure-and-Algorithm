from node import Node
from list import List

class SinglyList(List):
    def __init__(self):
        super().__init__(None, 0)

    def insertAtFirst(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def insertAt(self, data, index: int):
        node: Node = Node(data)
        if index < 1 or index > self.size + 1:
            self.outOfBound(index)

        elif index == 1:
            self.insertAtFirst(data)

        else:
            current: Node = self.head; previous: Node = current; cnt: int = 1
            while cnt < index:
                previous = current
                current = current.next
                cnt += 1
            
            node.next = current
            previous.next = node
            self.size += 1

    def insertAtLast(self, data):
        node: Node = Node(data, None)
        if self.head:
            current: Node = self.head
            while current.next:
                current = current.next
            
            current.next = node
            self.size += 1
        else:
            self.head = node

    def removeAtFirst(self):
        if self.head:
            self.head = self.head.next
            
            self.size -= 1

    def removeAt(self, index: int):
        if index < 1 or index > self.size:
            self.outOfBound(index)

        elif index == 1:
            self.head = self.head.next

        else:
            current: Node = self.head; cnt: int = 1
            while cnt < index - 1:
                current = current.next
                cnt += 1

            current.next = current.next.next
            self.size -= 1

    def removeAtLast(self):
        if self.head:
            current: Node = self.head; cnt: int = 1
            while current.next:
                current = current.next
                cnt += 1
                if cnt == self.size-1:
                    break
            
            current.next = None
            self.size -= 1

    def printList(self):
        if self.head: 
            current: Node = self.head
            print('Head -> ', end='')
            while current.next:
                print(current.data, '-> ', end='')
                current = current.next
            print(current.data, '-> Null')
            print("List Size:", self.size)

        else:
            print('Empty List!')

    def reverse(self):
        if self.head:
            current: Node = self.head; previousPtr:Node = None; nextPtr:Node = current.next
            while current.next:
                current.next = previousPtr
                previousPtr = current
                current = nextPtr
                nextPtr = current.next
            current.next = previousPtr
            self.head = current