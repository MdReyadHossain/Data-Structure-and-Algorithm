from linear_search import LinearSearch
from binary_search import BinarySearch
from ternary_search import TernarySearch

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

    def testTernarySearch(list, item):
        ternarySearch = TernarySearch(list)
        test = ternarySearch.searchItem(item)
        print(test)

    # testLinearSearch(arr[:], 200)
    # testBinarySearch(arr[:], 900)
    testTernarySearch(arr[:], 800)

# 100, 200, 300, 400, 500, 600, 700, 800, 900
#  0    1    2    3    4    5    6    7    8
#           mid1                mid2
