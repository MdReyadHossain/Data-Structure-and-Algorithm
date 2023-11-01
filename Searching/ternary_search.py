from list import List


class TernarySearch(List):
    def __init__(self, list):
        super().__init__(list, len(list))
        self.index: int = None
        self.firstMid: int = None
        self.secondMid: int = None
        self.left: int = None
        self.right: int = None

    def searchItem(self, item):
        self.list.sort()
        print(self.list)
        while True:
            self.size = self.right - self.left
            self.firstMid = self.left + (self.size // 3)
            self.secondMid = self.right - (self.size // 3)
