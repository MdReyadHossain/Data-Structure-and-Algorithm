from node import Node
from list import List


class SinglyList(List):
    def __init__(self):
        super().__init__(None, 0)

    def insertAtFirst(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def insertAt(self, data, index: int):
        node: Node = Node(data)
        if index < 1 or index > self.size + 1:
            self.outOfBound(index)

        elif index == 1:
            self.insertAtFirst(data)

        else:
            currentPtr: Node = self.head
            previous: Node = currentPtr
            cnt: int = 1
            while cnt < index:
                previous = currentPtr
                currentPtr = currentPtr.next
                cnt += 1

            node.next = currentPtr
            previous.next = node
            self.size += 1

    def insertAtLast(self, data):
        node: Node = Node(data, None)
        if self.head:
            currentPtr: Node = self.head
            while currentPtr.next:
                currentPtr = currentPtr.next

            currentPtr.next = node
            self.size += 1
        else:
            self.head = node

    def removeAtFirst(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1

    def removeAt(self, index: int):
        if index < 1 or index > self.size:
            self.outOfBound(index)

        elif index == 1:
            self.head = self.head.next

        else:
            currentPtr: Node = self.head
            cnt: int = 1
            while cnt < index - 1:
                currentPtr = currentPtr.next
                cnt += 1

            currentPtr.next = currentPtr.next.next
            self.size -= 1

    def removeAtLast(self):
        if self.head:
            currentPtr: Node = self.head
            cnt: int = 1
            while currentPtr.next:
                currentPtr = currentPtr.next
                cnt += 1
                if cnt == self.size-1:
                    break

            currentPtr.next = None
            self.size -= 1

    def swapNode(self, index1, index2):
        if self.head and index1 < index2:
            currentPtrX: Node = self.head
            currentPtrY: Node = self.head
            previousX: Node = None
            previousY: Node = None
            cnt: int = 1
            while cnt < index1:
                previousX = currentPtrX
                currentPtrX = currentPtrX.next
                cnt += 1
            cnt = 1
            while cnt < index2:
                previousY = currentPtrY
                currentPtrY = currentPtrY.next
                cnt += 1
            nextPtrY = currentPtrY.next
            if index2 - index1 == 1:
                currentPtrY.next = currentPtrX
            else:
                previousY.next = currentPtrX
                currentPtrY.next = currentPtrX.next
            currentPtrX.next = nextPtrY
            if index1 == 1:
                self.head = currentPtrY
            else:
                previousX.next = currentPtrY

    def printList(self):
        if self.head:
            currentPtr: Node = self.head
            print('Head -> ', end='')
            while currentPtr.next:
                print(currentPtr.data, '-> ', end='')
                currentPtr = currentPtr.next
            print(currentPtr.data, '-> Null')
            print("List Size:", self.size)

        else:
            print('Empty List!')

    def reverse(self):
        if self.head:
            currentPtr: Node = self.head
            previousPtr: Node = None
            nextPtr: Node = currentPtr.next
            while currentPtr.next:
                currentPtr.next = previousPtr
                previousPtr = currentPtr
                currentPtr = nextPtr
                nextPtr = currentPtr.next
            currentPtr.next = previousPtr
            self.head = currentPtr

    # bubble sort approach
    def sortList(self):
        currentXPtr: Node = self.head
        currentYPtr: Node = self.head
        cnt: int = 1
        isSwap: bool = False
        for i in range(self.size):
            isSwap = False
            for j in range(1, self.size - i):
                currentXPtr = self.head
                currentYPtr = self.head
                cnt = 1
                while cnt < j:
                    currentXPtr = currentXPtr.next
                    cnt += 1
                currentYPtr = currentXPtr.next
                if currentXPtr.data > currentYPtr.data:
                    self.swapNode(j, j+1)
                    isSwap = True
            if isSwap == False:
                break
