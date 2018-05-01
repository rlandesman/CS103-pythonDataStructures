import unittest
import linked_list

class TestCases(unittest.TestCase):
    def test_IteratorObject_eq(self):
        list1 = linked_list.Pair(5, linked_list.Pair(6, None))
        myIterator = linked_list.ListIterator(list1)
        list2 = linked_list.Pair(5, linked_list.Pair(6, None))
        secondIterator = linked_list.ListIterator(list2)
        self.assertEqual(myIterator == secondIterator, True)

    def test_ObjectIterator(self):
        myList = linked_list.Pair(5, linked_list.Pair(6, None))
        thisIT = linked_list.object_iterator(myList)
        compareIterator = linked_list.ListIterator(myList)
        self.assertEqual(thisIT == compareIterator, True)

    def test_has_next_false(self):
        myList = None
        thisIT = linked_list.object_iterator(myList)
        self.assertEqual(linked_list.has_next(thisIT),False)

    def test_has_next(self):
        myList = linked_list.Pair(5, linked_list.Pair(6, None))
        thisIT = linked_list.object_iterator(myList)
        self.assertEqual(linked_list.has_next(thisIT),True)

    def test_next(self):
        myList = linked_list.Pair(4, linked_list.Pair(5, linked_list.Pair(6, None)))
        thisIT = linked_list.object_iterator(myList)
        self.assertEqual(linked_list.next(thisIT),4)

    def test_next_error(self):
        myList = linked_list.Pair(4, linked_list.Pair(5, linked_list.Pair(6, None)))
        thisIT = linked_list.object_iterator(myList)
        linked_list.next(thisIT)
        linked_list.next(thisIT)
        with self.assertRaises(StopIteration):
            linked_list.next(thisIT)

    def test_yield_iterator(self):
        myList = linked_list.Pair(4, linked_list.Pair(5, linked_list.Pair(6, None)))
        y = linked_list.yield_iterator(myList)
        self.assertEqual(next(y),4)

    def test_yield_iterator2(self):
        myList = linked_list.Pair(4, linked_list.Pair(5, linked_list.Pair(6, None)))
        y = linked_list.yield_iterator(myList)
        next(y) #4
        next(y) #5
        next(y) #6
        with self.assertRaises(StopIteration):
            next(y)

if __name__ == '__main__':
    unittest.main()
