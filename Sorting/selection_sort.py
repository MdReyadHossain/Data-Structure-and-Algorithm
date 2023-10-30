from list import List


class SelectionSort(List):
    def __init__(self, list: list):
        super().__init__(list, len(list), 'Selection Sort')
        self.select: int = None
        self.index: int = 0

    def ascendingSort(self):
        for i in range(self.size):
            self.select = self.list[i]
            # print(f'i {i}: {self.list}')
            for j in range(i+1, self.size):
                if self.list[j] < self.select:
                    self.select = self.list[j]
                    self.index = j
            # print(f'\tselect: {self.select}')
            self.list[self.index] = self.list[i]
            self.list[i] = self.select

    def descendingSort(self):
        for i in range(self.size):
            self.select = self.list[i]
            for j in range(i+1, self.size):
                if self.list[j] > self.select:
                    self.select = self.list[j]
                    self.index = j
            self.list[self.index] = self.list[i]
            self.list[i] = self.select
