from list import List


class Stack(List):
    def __init__(self, size: int) -> None:
        super().__init__(size)

    def push(self, data: int):
        if self.determineSize():
            self.list.append(data)
            return True
        print('Array size exceed! for data:', data)
        return False

    def pop(self):
        if len(self.list) > 0:
            self.list.pop()
            return True
        print('Empty array, could not perform pop() operation')
        return False

    def peek(self):
        if len(self.list) > 0:
            return self.list[len(self.list) - 1]
        print('Empty array')
        return False

    def printStack(self):
        currentIndex: int = len(self.list) - 1
        print('Stack: ')
        while currentIndex >= 0:
            print('\t', self.list[currentIndex])
            currentIndex -= 1

        if len(self.list) == 0:
            print('\t[]')
# 5 2 3 1 6
