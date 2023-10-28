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

    # def insertAt(self, data, index):
    
    def insertAtLast(self, data):
        node = Node(data)
        if self.head:
            current: Node = self.head
            while current.next:
                current = current.next
            current.next = node
            node.previous = current
        else:
            self.head = node
        self.size += 1
    
    # def getNode(self, index):

    def printList(self):
        if self.head:
            current: Node = self.head

            print('Head <-> ', end='')
            while current.next:
                print(current.data, '<-> ', end='')
                current = current.next
            print(current.data, '<-> Null\n')

            print('Null <-> ', end='')
            while current.previous:
                print(current.data, '<-> ', end='')
                current = current.previous
            print(current.data, '<-> Head')
            
            print('List Size :', self.size)
        else:
            print('Empty List!')
