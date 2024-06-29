from stack import Stack

if __name__ == '__main__':
    def testStack():
        stacklist = Stack(3)
        stacklist.push(500)
        stacklist.push(400)
        stacklist.push(300)
        stacklist.printStack()

        print('Pop: ')
        print('\t', stacklist.pop())
        print('\t', stacklist.pop())
        print('\t', stacklist.pop())
        stacklist.printStack()

    def testQueue():
        print()

    testStack()
