from linear_search import LinearSearch
from binary_search import BinarySearch

if __name__ == '__main__':
    arr: list = [7, 4, 2, 3, 8, 1, 5, 6]

    def testLinearSearch(list, item):
        linearSearch = LinearSearch(list)
        test = linearSearch.searchItem(item)
        print(test)

    def testBinarySearch(list, item):
        binarySearch = BinarySearch(list)
        test = binarySearch.searchItem(item)
        print(test)

    # testLinearSearch(arr, 6)
    testBinarySearch(arr, 1)
