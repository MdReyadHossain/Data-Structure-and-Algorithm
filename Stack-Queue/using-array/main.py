from stack import Stack
from queue import Queue

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
        print()

    def testQueue():
        queueList = Queue(3)
        queueList.enqueue(500)
        queueList.enqueue(400)
        queueList.enqueue(300)
        queueList.printQueue()

        print('Dequeue: ')
        sl: int = 1
        while not queueList.isEmpty():
            print(f'\t{sl}. ', queueList.dequeue())
            sl += 1
        print(f'\t ', queueList.dequeue())
        print()

    testStack()
    testQueue()
