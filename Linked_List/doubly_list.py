from node import Node

class DoublyList:
    def __init__(self):
        self.head: Node = None
        self.size: int = 0
    
    def insertAtFirst(self, data):
        node = Node(data)
        if self.head:
            self.head.previous = node
            node.next = self.head
        self.head = node
        self.size += 1
    
    def insertAtLast(self, data):
        print()
    
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
