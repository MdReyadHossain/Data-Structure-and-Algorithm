from list import List


class Queue(List):
    def __init__(self, size: int) -> None:
        super().__init__(size)

    def enqueue(self, data: int):
        if self.size > self.tail:
            self.list.append(data)
            self.tail += 1
            return data
        return "List size out of range"
    
    def dequeue(self):
        if self.isEmpty():
            return "Empty list"
        
        front: int = self.list[0]
        for i in range(self.tail):
            self.list[i] = self.list[i + 1]
        self.tail -= 1
        return front
    
    def printQueue(self):
        print('Queue:')
        if len(self.list) > 0:
            for i in range(self.tail + 1):
                print(f'\t{i + 1}.', self.list[i])
        else:
            print("Empty list")

