class List:
    def __init__(self, head=None, size: int = 0):
        self.head = head
        self.size = size
        self.tail = None

    def isEmptyList(self):
        return self.head is None
