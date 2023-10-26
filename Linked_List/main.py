from singly_list import SinglyList

list = SinglyList()
list.insertAtFirst(400)
list.insertAtFirst(200)
list.insertAtLast(500)
list.insertAt(100, 1)
list.insertAt(300, 3)
list.insertAt(600, 6)

list.removeAtFirst()
list.removeAtLast()
list.removeAt(3)

list.printList()