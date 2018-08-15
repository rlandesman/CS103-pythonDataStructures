import unittest
from array_list import *

class TestCases(unittest.TestCase):
    def test_length1(self):
        myList = empty_list()
        self.assertEqual(length(myList),0)

    def test_eq(self):
        myList = empty_list()
        secondList = empty_list()
        self.assertEqual(myList,secondList)

    def test_empty(self):
        myList = empty_list()
        self.assertEqual(str(myList), 'Array([None, None, None, None, None, None, None, None, None, None], Size 0)')

    def test_length2(self):
        myList = empty_list()
        myList.size = 1
        self.assertEqual(length(myList),1)

    def test_add_empty(self):
        myList = empty_list()
        compareList = empty_list()
        compareList.array[0] = 90
        compareList.size = 1
        self.assertEqual(add(myList,0,90),compareList)

    def test_add_mid(self):
        myList = empty_list()
        myList.size = 3
        myList.array[0] = 1
        myList.array[1] = 2
        myList.array[2] = 3

        compareList = empty_list()
        compareList.size = 4
        compareList.array[0] = 1
        compareList.array[1] = 2
        compareList.array[2] = 99
        compareList.array[3] = 3

        self.assertEqual(add(myList,2,99),compareList)



if __name__ == '__main__':
    unittest.main()
