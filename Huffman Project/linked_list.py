
import unittest

# A Pair object has a value (any object) and either:
#   -None
#   -Another Pair object
class Pair():
    def __init__(self,first,rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest #Test

    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.first, self.rest)) #Test

    def __iter__(self):
        thisPair = self
        while thisPair != None:
            yield thisPair.first
            thisPair = thisPair.rest

# Data Definition AnyPair
# AnyPair is linked list of pair objects

#No input -> AnyPair
# returns an empty AnyPair list
def empty_list():
    return None
#self.assertEqual(empty_list(),Pair(None,None))

# AnyPair, int, AnyValue ->
#def add(list,index,value)

#AnyPair -> int
# returns the number of Pairs in the list
def length(list):
    if list == None:
        return 0
    return 1 + length(list.rest)

#AnyPair, Int, Int -> AnyPair
# Utilizes add_help method
def add(myList, index, value):
    if index < 0 or index > length(myList):
        raise IndexError #Test

    elif myList == None:
        newNode = Pair(value,None)
        return newNode

    elif index == 0:
        current = myList
        newNode = Pair(value,None)
        newNode.rest = current
        current = newNode
        return current
    else:
        current = myList
        previous = None
        for x in range(index):
            previous = current
            current = current.rest
        newNode = Pair(value,None)
        newNode.rest = current
        previous.rest = newNode
    return myList

# LinkedList, Node, Function -> LinkedList
def insert_sorted(sortedList, node, comes_before):
    idx = 0

    if sortedList is None:
        return Pair(node,None)
    else:
        for x in sortedList:
            if not comes_before(node,x):
                idx += 1
        sortedList = add(sortedList,idx,node)
    return sortedList

