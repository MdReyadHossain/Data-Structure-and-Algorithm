from stack import Stack

if __name__ == '__main__':
    def testStack():
        stacklist = Stack()
        stacklist.push(400)
        stacklist.push(300)
        stacklist.push(500)
        stacklist.push(100)

        stacklist.printStack()

        while stacklist.head:
            print(stacklist.peek())
            stacklist.pop()

    testStack()
