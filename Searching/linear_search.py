from list import List

class LinearSearch(List):
    def __init__(self, list):
        super().__init__(list, len(list))
        self.index = None

    def searchItem(self, item):
        for i in range(self.size):
            if self.list[i] == item:
                self.index = i
                break
        self.printResult(item, self.index)
        self.index = None
        return self.status
        
            