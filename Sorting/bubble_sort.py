from list import List

class BubbleSort(List):
    def __init__(self, list: list):
        super().__init__(list, len(list), 'Bubble Sort')

    def ascendingSort(self):
        arr: list = self.list; size: int = self.size
        isSwap: bool = False

        for i in range(size):
            isSwap = False
            print(f'\nPhase-{i+1}: {arr}')
            for j in range(0, size - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j] = arr[j] + arr[j+1]
                    arr[j+1] = arr[j] - arr[j+1]
                    arr[j] = arr[j] - arr[j+1]
                    isSwap = True
                print(f'\t{j+1}. {arr}')
            if isSwap == False:
                break

    def descendingSort(self):
        arr: list = self.list; size: int = self.size
        isSwap: bool = False

        for i in range(size):
            isSwap = False
            print(f'\nPhase-{i+1}: {arr}')
            for j in range(0, size - i - 1):
                if arr[j] < arr[j+1]:
                    arr[j] = arr[j] + arr[j+1]
                    arr[j+1] = arr[j] - arr[j+1]
                    arr[j] = arr[j] - arr[j+1]
                    isSwap = True
                print(f'\t{j+1}. {arr}')
            if isSwap == False:
                break
