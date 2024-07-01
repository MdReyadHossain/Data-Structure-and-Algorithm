from stack import Stack
from queue import Queue
from circular_queue import CircularQueue

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
        queueList.enqueue(200)
        queueList.printQueue()

        print("Peek: ", queueList.peek())

        print('\nDequeue: ')
        sl: int = 1
        while not queueList.isEmptyQueue():
            print(f'\t{sl}. ', queueList.dequeue())
            sl += 1
        print()

    def testCircularQueue():
        circularQueue = CircularQueue(3)
        circularQueue.enqueue(500)
        circularQueue.enqueue(400)
        circularQueue.enqueue(300)
        circularQueue.enqueue(200)
        circularQueue.printQueue()

        sl: int = 1
        print('\nDequeue: ')
        while not circularQueue.isEmptyQueue():
            print(f'\t{sl}.', circularQueue.dequeue())
            sl += 1
        print()

    # testStack()
    # testQueue()
    testCircularQueue()
