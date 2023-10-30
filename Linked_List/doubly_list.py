from node import Node
from list import List

class DoublyList(List):
    def __init__(self):
        super().__init__(None, 0)
    
    def insertAtFirst(self, data):
        node = Node(data)
        if self.head:
            self.head.previous = node
            node.next = self.head
        self.head = node
        self.size += 1 

    def insertAt(self, data, index):
        node = Node(data)
        if index == 1:
            self.insertAtFirst(data)
        elif index > 0 and index <= self.size + 1:
            currentPtr: Node = self.head; cnt: int = 1
            while cnt < index - 1:
                currentPtr = currentPtr.next
                cnt += 1
            if index <= self.size:
                node.next = currentPtr.next
                nextVal: Node = currentPtr.next
                nextVal.previous = node
            currentPtr.next = node
            node.previous = currentPtr
            self.size += 1
        else:
            self.outOfBound(index)
    
    # def insertAt(self, data, index):
    #     if :
            

    def insertAtLast(self, data):
        node = Node(data)
        if self.head:
            currentPtr: Node = self.head
            while currentPtr.next:
                currentPtr = currentPtr.next
            currentPtr.next = node
            node.previous = currentPtr
        else:
            self.head = node
        self.size += 1

    def removeAtFirst(self):
        if self.head:
            nextVal: Node = self.head.next
            self.head = nextVal
            if self.size > 1:
                nextVal.previous = None
            self.size -= 1

    def removeAt(self, index):
        if self.head:
            if index == 1:
                self.removeAtFirst()
            else:
                currentPtr: Node = self.head; previousPtr: Node; cnt: int = 1
                while cnt < index:
                    previousPtr = currentPtr
                    currentPtr = currentPtr.next
                    cnt += 1
                if currentPtr.next:
                    nextPtr: Node = currentPtr.next
                    nextPtr.previous = previousPtr
                previousPtr.next = currentPtr.next
                self.size -= 1

    def removeAtLast(self):
        if self.head:
            currentPtr: Node = self.head
            while currentPtr.next:
                currentPtr = currentPtr.next
            if self.size > 1:
                prevPtr: Node = currentPtr.previous
                prevPtr.next = None
            else:
                self.head = None
            self.size -= 1

    def printList(self):
        if self.head:
            currentPtr: Node = self.head

            print('Head <-> ', end='')
            while currentPtr.next:
                print(currentPtr.data, '<-> ', end='')
                currentPtr = currentPtr.next
            print(currentPtr.data, '<-> Null\n')

            print('Null <-> ', end='')
            while currentPtr.previous:
                print(currentPtr.data, '<-> ', end='')
                currentPtr = currentPtr.previous
            print(currentPtr.data, '<-> Head')
            
            print('List Size :', self.size)
        else:
            print('Empty List!')

    def reverse(self):
        currentPtr: Node = self.head
        previousPtr: Node = None
        nextPtr: Node = currentPtr.next

        while currentPtr.next:
            currentPtr.next = previousPtr
            currentPtr.previous = nextPtr
            previousPtr = currentPtr
            currentPtr = nextPtr
            nextPtr = currentPtr.next
        currentPtr.next = previousPtr
        currentPtr.previous = None
        self.head = currentPtr
