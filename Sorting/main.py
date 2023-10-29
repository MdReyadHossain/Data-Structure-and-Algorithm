from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
if __name__ == "__main__":
    arr: list = [7, 4, 2, 3, 8, 1, 5, 6]
    # arr: list = [1, 2, 3, 4, 5, 6, 7, 8]
    def testBubbleSort(list):
        bubbleSort = BubbleSort(list)
        bubbleSort.ascendingSort()
        bubbleSort.printList('Ascending List')

    def testInsertionSort(list):
        insertionSort = InsertionSort(list)
        insertionSort.ascendingSort()
        insertionSort.printList('Ascending List')

    testBubbleSort(arr)
    testInsertionSort(arr)