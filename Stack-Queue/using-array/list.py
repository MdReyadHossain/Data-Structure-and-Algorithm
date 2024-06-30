class List:
    def __init__(self, size: int) -> None:
        self.list = [] * size
        self.size = size
        self.tail = -1
        self.head = -1

    def determineSize(self):
        return len(self.list) < self.size
