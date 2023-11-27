from singly_list import SinglyList
from doubly_list import DoublyList
from circular_singly import CircularSinglyList
from cirular_doubly import CircularDoublyList

if __name__ == '__main__':
    def testSinglyList():
        print('\n')
        print('Singly List:')
        singlyList = SinglyList()
        singlyList.insertAtFirst(400)
        singlyList.insertAtFirst(200)
        singlyList.insertAt(100, 2)

        # singlyList.insertAt(300, 3)

        # singlyList.insertAtLast(500)
        # singlyList.removeAtFirst()
        # singlyList.removeAtLast()
        # singlyList.removeAt(3)

        # singlyList.getNode(1)
        singlyList.printList()
        print('\nReverse List:')
        singlyList.reverse()
        singlyList.printList()
        # print('\nSorted List:')
        # singlyList.sortList()
        # singlyList.printList()

    def testDoublyList():
        print('\n')
        print('Doubly List:')
        doublyList = DoublyList()
        doublyList.insertAtFirst(400)
        doublyList.insertAtFirst(200)
        doublyList.insertAtFirst(100)
        doublyList.insertAtLast(500)
        doublyList.insertAtLast(600)
        doublyList.insertAt(300, 3)

        doublyList.removeAtFirst()
        doublyList.removeAt(1)
        doublyList.removeAtLast()

        doublyList.printList()
        print('\nReverse List:')
        doublyList.reverse()
        doublyList.printList()

    def testCircualarSingly():
        print('\n')
        print('Circular Singly List:')
        circualrSinglyList = CircularSinglyList()
        circualrSinglyList.inserAtFirst(200)
        circualrSinglyList.inserAtFirst(100)
        circualrSinglyList.insertAtLast(400)
        circualrSinglyList.insertAtLast(500)
        circualrSinglyList.insertAt(300, 3)
        circualrSinglyList.printList()
        print('\nAfter Remove: ')
        # circualrSinglyList.removeAtFirst()
        circualrSinglyList.removeAt(7)
        circualrSinglyList.printList()
        # circualrSinglyList.getNode(4)
        # circualrSinglyList.getNextNode(3)

    def testCircualarDoubly():
        circularDoublyList = CircularDoublyList()
        circularDoublyList.insertAtFirst(300)
        circularDoublyList.insertAtFirst(200)
        circularDoublyList.insertAtFirst(100)
        circularDoublyList.insertAtLast(500)
        circularDoublyList.insertAtLast(600)
        circularDoublyList.insertAt(400, 4)
        circularDoublyList.printList()
        circularDoublyList.removeAtFirst()
        circularDoublyList.removeAtLast()
        circularDoublyList.removeAt(1)
        circularDoublyList.printList()

    # testSinglyList()
    # testDoublyList()
    # testCircualarSingly()
    testCircualarDoubly()
