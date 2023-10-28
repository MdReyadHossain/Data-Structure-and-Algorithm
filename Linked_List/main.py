from singly_list import SinglyList
from doubly_list import DoublyList

def testSinglyList():
    print('\n')
    print('Singly List:')
    singlyList = SinglyList()
    singlyList.insertAtFirst(400)
    singlyList.insertAtFirst(200)
    singlyList.insertAtLast(500)
    singlyList.insertAt(100, 1)
    singlyList.insertAt(300, 3)
    singlyList.insertAt(600, 6)

    singlyList.removeAtFirst()
    singlyList.removeAtLast()
    singlyList.removeAt(3)

    singlyList.getNode(1)
    singlyList.printList()
    print('\nReverse List:')
    singlyList.reverse()
    singlyList.printList()


def testDoublyList():
    print('\n')
    print('Doubly List:')
    doublyList = DoublyList()
    doublyList.insertAtFirst(400)
    doublyList.insertAtFirst(200)
    doublyList.insertAtFirst(100)
    doublyList.insertAtLast(500)
    doublyList.getNode(4)
    doublyList.printList()
    

testSinglyList()
testDoublyList()
