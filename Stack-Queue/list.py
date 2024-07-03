class List:
    def __init__(self, head, size: int):
        self.head = head
        self.size = size
        self.tail = None

    def isEmptyList(self):
        if self.head is None:
            print('Empty List!')
            return True
        return False
