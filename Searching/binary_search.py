from list import List


class BinarySearch(List):
    def __init__(self, list):
        super().__init__(list, len(list))
        self.index: int = None
        self.left: int = 0
        self.right: int = self.size - 1

    def searchItem(self, item):
        self.list.sort()
        size: int = self.right - self.left
        mid: int = size//2
        while self.left <= self.right:
            # print(f'\t{self.left} --- {self.right}')
            size = self.right - self.left
            mid = self.left + (size//2)
            if self.list[mid] > item:
                self.right = mid - 1
            elif self.list[mid] < item:
                self.left = mid + 1
            else:
                self.index = mid
                break
            # print(f'\tmid = {mid}')
            # print(f'\tvalue = {self.list[mid]}')
        self.printResult(item, self.index)
        return self.status
