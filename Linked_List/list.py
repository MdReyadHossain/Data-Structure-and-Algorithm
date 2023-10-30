from node import Node
class List:
    def __init__(self, head: Node, size: int):
        self.head = head
        self.size = size

    def outOfBound(self, index: int):
        print(f'Error: Index {index} is out of bound!')