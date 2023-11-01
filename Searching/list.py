class List:
    def __init__(self, list: list, size: int):
        self.list = list
        self.size = size
        self.status: bool = False

    def printResult(self, item, index):
        if index or index == 0:
        if index or index == 0:
            print(f'{item} found at index {index}!')
            self.status = True
        else:
            print(f'{item} not found!\nindex: {index}')
            self.status = False
