class List:
    def __init__(self, size: int) -> None:
        self.list = [] * size
        self.size = size
        self.tail = -1
        
    def isEmpty(self):
        return self.tail == -1

    def determineSize(self):
        return len(self.list) < self.size
