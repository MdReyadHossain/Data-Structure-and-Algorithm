from list import List
from node import Node


class CircularDoublyList(List):
    def __init__(self):
        super().__init__(None, 0)
        self.tail = None
