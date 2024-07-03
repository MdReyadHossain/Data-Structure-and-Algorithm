from stack import Stack
from queue import Queue
from circular_queue import CircularQueue

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
        queueList = Queue()
        queueList.enqueue(10)
        queueList.enqueue(20)
        queueList.enqueue(30)
        queueList.printQueue()

        print('Dequeue: ')
        while not queueList.isEmptyList():
            print('\t', queueList.dequeue())

    def testCircularQueue():
        circularQueue = CircularQueue()
        circularQueue.enqueue(500)
        circularQueue.enqueue(400)
        circularQueue.enqueue(300)
        circularQueue.enqueue(200)
        circularQueue.printQueue()

        sl: int = 1
        print('\nDequeue: ')
        while not circularQueue.isEmptyList():
            print(f'\t{sl}.', circularQueue.peek(), '-> dequeue')
            circularQueue.dequeue()
            sl += 1
        print()

    # testStack()
    # testQueue()
    testCircularQueue()
