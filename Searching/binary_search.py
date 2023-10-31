from list import List

class BinarySearch(List):
    def __init__(self, list):
        super().__init__(list, len(list))
        self.index: int = None
        self.min: int = 0
        self.max: int = self.size - 1

    def searchItem(self, item):
        self.list.sort()
        print(self.list)
        size: int = self.max - self.min
        while True:
            if self.list[mid] > item:
                self.max = mid - 1
                mid: int = int(size/2)
                size: int = self.max - self.min
            elif self.list[mid] < item:
                self.min = mid + 1
                mid: int = int(size/2) + self.min
            else:
                self.index = mid
                self.printResult(item, self.index)
                break
            print(f'middle = {mid}')
            print(f'{self.min} -- {self.max}')
        print(f'middle = {mid}')
        print(f'{self.min} -- {self.max}')
        return self.status
