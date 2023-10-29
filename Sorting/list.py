class List:
    def __init__(self, list: list, size: int, sort: str):
        self.list = list
        self.size = size
        self.sort = sort

    def printList(self, type: str):
        print(f'{self.sort}:')
        print(f'{type}: {self.list}')