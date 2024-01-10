from stack import Stack

if __name__ == '__main__':
    def testStack():
        stacklist = Stack(3)
        stacklist.push(400)
        stacklist.push(300)
        stacklist.printStack()

        print('Peek')
        print('\t', stacklist.peek())
        stacklist.pop()
        print('\t', stacklist.peek())
        stacklist.pop()
        print('\t', stacklist.peek())
        stacklist.pop()
        stacklist.printStack()

    def testQueue():
        print()

    testStack()
