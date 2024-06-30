from list import List


class Queue(List):
    def __init__(self, size: int) -> None:
        super().__init__(size)

    def isEmptyQueue(self):
        return self.tail == -1

    def enqueue(self, data: int):
        if self.size > self.tail + 1:
            self.list.append(data)
            self.tail += 1
            return data
        print("Out of range for store:", data)
        return None

    def dequeue(self):
        if self.isEmptyQueue():
            return "Empty list"

        front: int = self.list[0]
        for i in range(self.tail):
            self.list[i] = self.list[i + 1]
        self.tail -= 1
        return front

    def peek(self):
        if self.isEmptyQueue():
            return "Empty list"

        return self.list[0]

    def printQueue(self):
        print('Queue:')
        if not self.isEmptyQueue():
            for i in range(self.tail + 1):
                print(f'\t{i + 1}.', self.list[i])
        else:
            print("Empty list")
