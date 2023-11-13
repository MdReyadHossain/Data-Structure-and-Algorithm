from list import List


class MergeSort(List):
    def __init__(self, list: list):
        super().__init__(list, len(list), 'Merge Sort')
        self.left: int = 0
        self.right: int = len(self.list) - 1

    def conquer(self, left, right, mid, asc):
        index1 = left
        index2 = mid + 1
        merge = []
        # print(f'{left} --- {right}')

        while index1 <= mid and index2 <= right:
            if (self.list[index1] < self.list[index2] and asc == True) or (self.list[index1] > self.list[index2] and asc == False):
                merge.append(self.list[index1])
                index1 += 1
            else:
                merge.append(self.list[index2])
                index2 += 1

        while index1 <= mid:
            merge.append(self.list[index1])
            index1 += 1

        while index2 <= right:
            merge.append(self.list[index2])
            index2 += 1

        indexTemp: int = left
        for i in range(len(merge)):
            self.list[indexTemp] = merge[i]
            indexTemp += 1
        # print(f'{merge}')

    def devide(self, left: int, right: int, asc: bool):
        if left >= right:
            return
        mid = int(left + (right - left)/2)
        self.devide(left, mid, asc)
        self.devide(mid + 1, right, asc)
        self.conquer(left, right, mid, asc)

    def ascendingSort(self):
        self.devide(self.left, self.right, True)

    def descendingSort(self):
        self.devide(self.left, self.right, False)
