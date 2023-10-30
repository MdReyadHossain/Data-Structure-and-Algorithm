class List:
    def __init__(self, list: list, size: int):
        self.list = list
        self.size = size
        self.status: bool = False

    def printResult(self, item, index):
        if index:
            print(f'{item} found at index {index}!')
            self.status = True
        else:
            print(f'{item} not found!')
            self.status = False