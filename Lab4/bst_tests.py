import unittest
from bst import *

def test_func(a):
    return a*2

def test_comes_before_int(a,b):
    if not(a < b) and not(b < a):
        return True
    elif a < b:
        return True
    else:
        return False

class TestCases(unittest.TestCase):
    def test_eq_none(self): #BST EQ
        myBST = BinarySearchTree(None,test_func(5))
        tree = BinarySearchTree(BST(5,6,7),test_func(5))
        self.assertEqual(myBST.BST == tree.BST, False)

    def test_eq_true(self): #BST EQ
        myBST = BinarySearchTree(BST(5,None,None), test_func(5))
        myBST2 = BinarySearchTree(BST(5,None,None), test_func(5))
        self.assertEqual(myBST.BST == myBST2.BST, True)

    def test_eq_searchTree(self): #BinarySearchTree EQ
        myBST = BinarySearchTree(BST(5,None,None), test_func(5))
        myBST2 = BinarySearchTree(BST(5,None,None), test_func(5))
        self.assertEqual(myBST == myBST2, True)

    def test_eq_searchTree_false(self): #BinarySearchTree EQ
        myBST = BinarySearchTree(BST(5,None,None), test_func(5))
        myBST2 = BinarySearchTree(None, test_func(5))
        self.assertEqual(myBST == myBST2, False)

    def test_is_empty_false(self):
        myTree = BST(42,None,None)
        myBST = BinarySearchTree(myTree,test_func(5))
        self.assertEqual(is_empty(myBST),False)

    def test_is_empty_true(self):
        myTree = None
        myBST = BinarySearchTree(myTree,test_func(5))
        self.assertEqual(is_empty(myBST),True)

    # def test_insert(self):
    #     myTree = BST(50, None, None)
    #     myTree.right = BST(70, None, None)
    #     myTree.left = BST(30, None, None)
    #     myBST = BinarySearchTree(myTree, test_comes_before_int)
    #     returnTree = insert(myBST,60)
    #     print(returnTree.BST.left.BST.root)

if __name__ == '__main__':
    unittest.main()

#Current Questions:
    # How do I test the insert method, specifically the comes_before
    # What do I return for comes_before given tht the inputTree is empty
