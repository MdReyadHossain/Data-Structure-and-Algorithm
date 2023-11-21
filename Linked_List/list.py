from node import Node

class List:
    def __init__(self, head: Node, size: int):
        self.head = head
        self.size = size
    
    def getNode(self, index):
        if index > 0 and index <= self.size:
            current: Node = self.head; cnt: int = 1
            while cnt < index:
                current = current.next
                cnt += 1
            print(current.__dict__)
        else:
            self.outOfBound(index)

    def outOfBound(self, index: int):
        print(f'Error: Index {index} is out of bound!')
        