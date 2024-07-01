from list import List


class CircularQueue(List):
    def __init__(self, size: int) -> None:
        super().__init__(size)

    def isEmptyQueue(self):
        return self.tail == -1

    def isFullQueue(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, data: int):
        if self.isFullQueue():
            print(f"List is full, {data} not added to queue")
            return False
        if self.isEmptyQueue():
            self.head = self.tail = 0
            self.list[self.tail] = data
            return data
        # rear = (rear + 1) % array_size
        self.tail = (self.tail + 1) % self.size
        self.list[self.tail] = data
        return data

    def dequeue(self):
        if self.isEmptyQueue():
            return "Queue is empty"
        data: int = self.list[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
            return data
        self.head += 1 % self.size
        return data

    def peek(self):
        if self.isEmptyQueue():
            return "Queue is empty"
        return self.list[self.head]

    def printQueue(self):
        if self.isEmptyQueue():
            return "Queue is empty"
        print("Queue:")
        i = self.head
        while True:
            if i == self.tail:
                print(f'\t {i + 1}.', self.list[i])
                break
            print(f'\t {i + 1}.', self.list[i])
            i += 1 % self.size
        return
