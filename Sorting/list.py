class List:
    def __init__(self, list: list, size: int, sort: str):
        self.list = list
        self.size = size
        self.sort = sort
        self.limitationError() if self.size < 2 else None

    def limitationError(self):
        print('Minimum length should be 2')
        exit()

    def printList(self, type: str):
        print(f'{self.sort}:')
        print(f'{type}: {self.list}')
