from list import List


class InsertionSort(List):
    def __init__(self, list):
        super().__init__(list, len(list), 'Insertion Sort')
        self.key = 0

    def ascendingSort(self):
        for i in range(1, self.size):
            self.key = self.list[i]
            # print(f'i {i}: {self.list} key: {self.key}')
            for j in range(i-1, -2, -1):
                if j == -1 or (self.list[j] <= self.key and j < i - 1):
                    self.list[j + 1] = self.key
                    break
                elif self.list[j] > self.key:
                    self.list[j + 1] = self.list[j]
                else:
                    break
                # print(f'\tj {j}: {self.list}')

    def descendingSort(self):
        for i in range(1, self.size):
            self.key = self.list[i]
            # print(f'i {i}: {self.list} key: {self.key}')
            for j in range(i-1, -2, -1):
                if j == -1 or (self.list[j] >= self.key and j < i - 1):
                    self.list[j + 1] = self.key
                    break
                elif self.list[j] < self.key:
                    self.list[j + 1] = self.list[j]
                else:
                    break
                # print(f'\tj {j}: {self.list}')
