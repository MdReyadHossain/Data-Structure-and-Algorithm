from list import List


class TernarySearch(List):
    def __init__(self, list):
        super().__init__(list, len(list))
        self.index: int = None
        self.firstMid: int = None
        self.secondMid: int = None
        self.left: int = 0
        self.right: int = self.size - 1

    def searchItem(self, item):
        self.list.sort()
        print(self.list)
        while True:
            self.size = self.right - self.left
            self.firstMid = self.left + (self.size // 3)
            self.secondMid = self.right - (self.size // 3)

            if self.list[self.firstMid] == item:
                self.index = self.firstMid
                break
            elif self.list[self.secondMid] == item:
                self.index = self.secondMid
                break
            elif self.list[self.firstMid] > item:
                self.left = self.firstMid - 1
            elif self.list[self.secondMid] < item:
                self.right = self.secondMid + 1
            elif self.list[self.firstMid] < item:
                self.left = self.firstMid + 1
                self.right = self.secondMid - 1
        self.printResult(item, self.index)
        return self.status
