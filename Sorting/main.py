from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from selection_sort import SelectionSort


if __name__ == '__main__':
    arr: list = [7, 4, 2, 3, 8, 1, 5, 6]
    # arr: list = [7]
    # arr: list = [1, 2, 3, 4, 5, 6, 7, 8]

    def testBubbleSort(list):
        bubbleSort = BubbleSort(list)
        bubbleSort.ascendingSort()
        bubbleSort.printList('Ascending List')

    def testInsertionSort(list):
        insertionSort = InsertionSort(list)
        insertionSort.ascendingSort()
        insertionSort.printList('Ascending List')

    def testSelectionSort(list):
        selectionSort = SelectionSort(list)
        selectionSort.ascendingSort()
        selectionSort.printList('Ascending List')

    testBubbleSort(arr)
    # # testInsertionSort(arr)
    # testSelectionSort(arr)
