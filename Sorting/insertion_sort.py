from list import List

class InsertionSort(List):
    def __init__(self, list):
        super().__init__(list, len(list), 'Insertion Sort')
        self.key = 0

    def ascendingSort(self):
        arr: list = self.list; size: int = self.size
        
        for i in range(1, size):
            self.key = arr[i]
            print(f'i {i}: {arr} key: {self.key}')
            for j in range(i-1, -2, -1):
                if j == -1 or (arr[j] <= self.key and j < i - 1):
                    arr[j + 1] = self.key
                    break
                elif arr[j] > self.key:
                    arr[j + 1] = arr[j]
                else:
                    break
                print(f'\tj {j}: {arr}')

    def descendingSort(self):
        arr: list = self.list; isSwap: bool = False
        for i in range(len(arr)):
            isSwap = False
            print(f'\nPhase-{i+1}: {arr}')
            for j in range(0, len(arr) - i - 1):
                if arr[j] < arr[j+1]:
                    arr[j] = arr[j] + arr[j+1]
                    arr[j+1] = arr[j] - arr[j+1]
                    arr[j] = arr[j] - arr[j+1]
                    isSwap = True
                print(f'\t{j+1}. {arr}')
            if isSwap == False:
                break
