from list import List


class CircularQueue(List):
    def __init__(self, size: int) -> None:
        super().__init__(size)

    def isEmptyQueue(self):
        return self.tail == -1
