from linked_list import *
import unittest
import huffman

class TestCases(unittest.TestCase):
    def test_length_empty(self):
        myList = None
        self.assertEqual(length(myList),0)

    def test_length_empty1(self):
        my_list = Pair(5 ,None)
        self.assertEqual(length(my_list),1)

    def test_length_1(self):
        oneList = Pair(None,None)
        self.assertEqual(length(oneList),1)

    def test_length(self):
        my_list = Pair(5, Pair(10, Pair(15, Pair(20, Pair(25, None)))))
        self.assertEqual(length(my_list), 5)

    def test_length1(self):
        my_list = Pair(5, Pair(10, None))
        self.assertEqual(length(my_list), 2)

    def test_pair_repr(self):
        myPair = Pair(5,None)
        self.assertEqual(myPair.__repr__(),"Pair(5, None)")

    def test_empty_list(self):
        self.assertEqual(empty_list(),None)

    def test_pair_eq(self):
        myPair = Pair(5,None)
        comparePair = Pair(6,None)
        vool = myPair == comparePair
        self.assertEqual(vool,False)

    def test_add_empty(self):
        testThis = add(empty_list(),0,5)
        myPair = Pair(5, None)
        self.assertEqual(testThis,myPair)

    def test_add_end(self):
        test_list = Pair(5, Pair(10, Pair(15, Pair(20, None))))
        compare_list = Pair(5, Pair(10, Pair(15, Pair(20, Pair(77, None)))))
        self.assertEqual(str(add(test_list,4,77)),str(compare_list))

    def test_add_mid(self):
        test_list = Pair(5, Pair(10, Pair(15, Pair(20, None))))
        compare_list = Pair(5, Pair(10, Pair(66, Pair(15, Pair(20, None)))))
        self.assertEqual(str(add(test_list,2,66)),str(compare_list))

    def test_add_empty2(self):
        test1 = (add(None,0,5))
        myPair = Pair(5, None)
        self.assertEqual(test1,myPair)

    def test_add_IE(self):
        with self.assertRaises(IndexError):
            add(Pair(5, Pair(10, Pair(15, None))), 4, 99)

    def test_add_IE2(self):
        with self.assertRaises(IndexError):
            add(empty_list(),-5,99)

    def test_pair_eq2(self):
        pair1 = Pair(5, None)
        pair2 = Pair(5, None)
        self.assertEqual(pair1 == pair2, True)

    def test_pair_eq_false(self):
        pair1 = Pair(6, None)
        pair2 = Pair(5, None)
        self.assertEqual(pair1 == pair2, False)

    def test_iter(self):
        myPair = Pair(5, None)
        gen = (iter(myPair))
        for x in gen:
            self.assertEqual(x,5)

    def test_insert_sorted_empty(self):
        empty = empty_list()
        myPair = 5
        self.assertEqual(insert_sorted(empty,myPair,huffman.comes_before),Pair(5, None))

    def test_insert_sorted(self):
        notEmpty = Pair(huffman.HuffmanTree(huffman.Leaf(54,2)),None)
        myPair = huffman.HuffmanTree(huffman.Leaf(42,3))
        compareList = Pair(huffman.HuffmanTree(huffman.Leaf(54,2)),Pair(huffman.HuffmanTree(huffman.Leaf(42,3)),None))
        ok = (insert_sorted(notEmpty,myPair,huffman.comes_before))
        self.assertEqual(ok,compareList)


if __name__ == '__main__':
    unittest.main()
