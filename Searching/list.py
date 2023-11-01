class List:
    def __init__(self, list: list, size: int):
        self.list = list
        self.size = size
        self.status: bool = False

    def printResult(self, item, index):
        if index or index == 0:
            print(f'Yes! {item} found!')
            self.status = True
        else:
            print(f'Oops! {item} not found!')
            self.status = False
