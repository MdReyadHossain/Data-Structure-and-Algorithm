class List:
    def __init__(self, list, size, sort):
        self.list = list
        self.size = size
        self.sort = sort

    def printList(self, type):
        print(f'{self.sort}:')
        print(f'{type}: {self.list}')