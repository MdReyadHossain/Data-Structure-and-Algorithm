class List:
    def __init__(self, size: int) -> None:
        self.list = [] * size
        self.size = size

    def determineSize(self):
        return len(self.list) < self.size
