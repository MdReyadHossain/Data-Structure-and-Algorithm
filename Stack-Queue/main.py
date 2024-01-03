from stack import Stack

if __name__ == '__main__':
    def testStack():
        stacklist = Stack()
        stacklist.push(400)
        stacklist.push(300)
        stacklist.push(500)
        stacklist.push(100)
        stacklist.printStack()

        print('Pop: ')
        sl: int = 1
        while stacklist.head:
            print(f'\t{sl}. ', stacklist.peek())
            sl += 1
            stacklist.pop()

    def testQueue():
        print()

    testStack()
