import unittest

# A Pair object has a value (any object) and either:
#   -None
#   -Another Pair object
class Pair():
    def __init__(self,first,rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.first == other.first and self.rest == other.rest

    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.first, self.rest))

class Song():
    def __init__(self, number, title, artist, album):
        self.number = number
        self.title = title
        self.artist = artist
        self.album = album

    def __eq__(self, other):
        if Song == None:
            return False
        else:
            return self.number == other.number and self.title == other.title and self.artist == other.artist and self.album == other.album

    def __repr__(self):
        return "Song = Number({!r}), Title({!r}), Artists{!r}), Album({!r})".format(self.number, self.title,
                                                                                    self.artist, self.album)

class ListIterator:
    def __init__(self,list):
        self.list = list
    def __eq__(self, other):
        if other == None:
            return False
        else:
            return self.list == other.list

#LinkedList -> ListIterator
def object_iterator(inputLinked):
    myIterator = ListIterator(inputLinked)
    return myIterator

def has_next(inputIterator):
    if inputIterator.list == None:
        return False
    else:
        if inputIterator.list.rest != None:
            return True
        else:
            return False

def next(inputIterator):
    if inputIterator == None:
        raise StopIteration

    elif has_next(inputIterator) is False:
        raise StopIteration

    else:
        currentVal = inputIterator.list.first #Current value
        inputIterator.list = inputIterator.list.rest #Move the list by one
        return currentVal

def yield_iterator(inputLinked):
    while inputLinked != None:
        yield inputLinked.first
        inputLinked = inputLinked.rest


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
#self.assertEqual(length(anyPair),x)

#AnyPair, Int, Int -> AnyPair
# Utilizes add_help method
def add(myList, index, value):
    if index < 0 or index > length(myList):
        raise IndexError

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

def add_beg(InputList,Value):
    current = InputList
    newNode = Pair(Value, None)
    newNode.rest = current
    current = newNode
    return current

# Pair, int, int -> value (of any type)
#return type is any
def get_help(list1, index, count):
    if index == count:
        return list1.first
    return get_help(list1.rest, index, count + 1)
#Tested in get method

#Pair, Int -> Value
def get(list, index):
    if 0 > index or index > length(list) - 1:
        raise IndexError
    else:
        return get_help(list, index, 0)
# self.assertEqual(get(my_anylist,1), "string")

def remove_help(list1, index, count):
    if index == count:
        if list1.rest is None:
            return None
        return Pair(list1.rest.first, list1.rest.rest)
    return Pair(list1.first, remove_help(list1.rest, index, count + 1))

# Pair, Int, Int -> Pair
#returns new AnyPair in which index has been changed to value
def set(list1, index, value):
    if 0 > index or index > length(list1) - 1:
        raise IndexError
    else:
        return set_help(list1, index, value, 0)

# Pair, int, int, int -> Pair
#returns a pair to be used in set function
def set_help(list1, index, value, count):
    if index == count:
        return Pair(value, list1.rest)
    return Pair(list1.first, set_help(list1.rest, index, value, count + 1))

# AnyPair, Int -> Tuple
#returns a tuple with the value of the removed element and the resulting AnyPair list
def remove(list, index):
    if 0 > index or index > length(list) - 1:
        raise IndexError
    else:
        return get(list, index), remove_help(list, index, 0)

#Abstract Data Type, Function -> None
# Returns none
# Calls function on each element
def foreach(ADT,function):
    if ADT == None:
        return None
    while ADT.rest != None:
        function(ADT.first)
        ADT = ADT.rest
    return None


def InsertionSort(list,key):
    if list == None:
        return None
    ReturnList = list
    list = list.rest #Current
    ReturnList.rest = None #Previous
    while list != None:
        current = list
        list = list.rest
        if ComparatorByKey(key, current.first, ReturnList.first) == False:
            current.rest = ReturnList
            ReturnList = current
        else:
            search = ReturnList
            while search.rest != None and ComparatorByKey(key, current.first, search.rest.first):
                search = search.rest
            current.rest = search.rest
            search.rest = current
    return ReturnList


def ComparatorByKey(user_input,a,b):
    if int(user_input) == 2:
        if a.artist == b.artist:
            return True
        if a.artist > b.artist:
            return True
        elif a.artist < b.artist:
            return False
        else:
            return(ComparatorByKey(3,a,b))

    if int(user_input) == 1:
        if a.title == b.title:
            return True
        if a.title > b.title:
            return True
        elif a.title < b.title:
            return False
        else:
            return(ComparatorByKey(0,a,b))

    if int(user_input) == 3:
        if a.album == b.album:
            return True
        if a.album > b.album:
            return True
        elif a.album < b.album:
            return False
        else:
            return(ComparatorByKey(1,a,b))

    if int(user_input) == 0:
        if a.number == b.number:
            return True
        if a.number > b.number:
            return True
        elif a.number < b.number:
            return False
        else:
            return(ComparatorByKey(2,a,b))



