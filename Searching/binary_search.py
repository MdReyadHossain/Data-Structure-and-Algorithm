from list import List
# from ..Sorting.bubble_sort import BubbleSort


class BinarySearch(List):
    def __init__(self, list):
        super().__init__(list, len(list))
        self.index: int = None
        self.min: int = 0
        self.max: int = self.size - 1

    def searchItem(self, item):
        # sort = BubbleSort(self.list)
        # sort.ascendingSort()
        print(self.list)
        # while True:
        #     size: int = self.max - self.min
        #     if self.list[int(size/2)] > item:
        #         self.max = int(size/2) - 1
        #     elif self.list[int(size/2)] < item:
        #         self.min = int(size/2) + 1
        #     else:
        #         self.index = int(size/2)
        #         self.printResult(item, self.index)
        #         break
