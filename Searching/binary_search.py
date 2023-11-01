from list import List

class BinarySearch(List):
    def __init__(self, list):
        super().__init__(list, len(list))
        self.index: int = None
        self.min: int = 0
        self.max: int = self.size - 1

    def searchItem(self, item):
        self.list.sort()
        size: int = self.max - self.min
        mid: int = size//2
        while self.min <= self.max:
            # print(f'\t{self.min} --- {self.max}')
            mid = (size//2) + self.min
            if self.list[mid] > item:
                self.max = mid - 1
                size = self.max - self.min
            elif self.list[mid] < item:
                self.min = mid + 1
                size = self.max - self.min
            else:
                self.index = mid
                break
            # print(f'\tmid = {mid}')
            # print(f'\tvalue = {self.list[mid]}')
        self.printResult(item, self.index)
        return self.status
