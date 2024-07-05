from list import List


class Fiboniacci(List):
    def __init__(self):
        super().__init__()

    def series(self,  end: int, i: int = 1):
        if i == end:
            self.arr[i] = self.arr[i - 2] + self.arr[i - 1]
            print(self.arr[i], end=" ")
            return self.arr
        if i == 1:
            print(i, end=" ")
            self.arr[i] = i
        else:
            self.arr[i] = self.arr[i - 2] + self.arr[i - 1]
            print(self.arr[i], end=" ")

        self.series(end, i+1)

    def nthValue(self, n: int):
        if n == 0 or n == 1:
            return n

        value: int = self.nthValue(n - 1) + self.nthValue(n - 2)
        return value
