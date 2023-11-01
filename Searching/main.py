from linear_search import LinearSearch
from binary_search import BinarySearch

if __name__ == '__main__':
    arr: list = [700, 400, 900, 200, 300, 800, 100, 500, 600]

    def testLinearSearch(list, item):
        linearSearch = LinearSearch(list)
        test = linearSearch.searchItem(item)
        print(test)

    def testBinarySearch(list, item):
        binarySearch = BinarySearch(list)
        test = binarySearch.searchItem(item)
        print(test)

    # testLinearSearch(arr, 6)
    testBinarySearch(arr, 650)

# 100 200 300 400 500 600 700 800
#  0   1   2   3   4   5   6   7