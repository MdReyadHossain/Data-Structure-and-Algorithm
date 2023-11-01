from list import List


class TernarySearch(List):
    def __init__(self, list):
        super().__init__(list, len(list))
        self.index: int = None
        self.firstMid: int = None
        self.secondMid: int = None

    def searchItem(self, item):
        self.list.sort()
        print(self.list)
