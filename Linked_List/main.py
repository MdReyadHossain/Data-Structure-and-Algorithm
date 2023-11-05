from singly_list import SinglyList
from doubly_list import DoublyList

if __name__ == '__main__':
    def testSinglyList():
        print('\n')
        print('Singly List:')
        singlyList = SinglyList()
        singlyList.insertAt(100, 1)
        singlyList.insertAtFirst(400)
        singlyList.insertAtFirst(200)

        singlyList.insertAt(300, 3)

        singlyList.insertAtLast(500)
        singlyList.removeAtFirst()
        singlyList.removeAtLast()
        singlyList.removeAt(3)

        singlyList.getNode(1)
        singlyList.printList()
        print('\nReverse List:')
        singlyList.reverse()
        singlyList.printList()
        print('\nSorted List:')
        singlyList.sortList()
        singlyList.printList()

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

    testSinglyList()
    testDoublyList()
