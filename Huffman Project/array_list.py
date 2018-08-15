class List():
    def __init__(self,capacity = 10):
        self.array = [None] * capacity #Built-in python list
        self.size = 0 #integer representing actual number of elements of array
        self.capacity = capacity

    def __eq__(self, other):
        return ((type(other) == List) and self.array == other.array and self.size == other.size and self.capacity == other.capacity)

    def __repr__(self):
        return "Array({!r}, Size {!r})".format(self.array,self.size)

# -> List object
# Takes in no parameter
# Returns a List object with zero length and an empty array
def empty_list():
    return List()
# self.assertEqual(repr(empty_list()),"Array([]), Length(0)")

# List -> integer
# Takes in a list object
# returns the length of list (in int form)
def length(list):
    return list.size
#self.assertEqual(length(myList),x) x being the returned length of myList

# List, int, int -> List
# InputList is a list object
# Index is an integer
# Value is an integer
# returns a list with an added element at position index and value 'value'
def add(arr,index,new_elt):
    if ((index > arr.size) or (index < 0)):
        raise IndexError
    # maybe_extend_array(arr)
    arr.size += 1
    for x in range(arr.size,index,-1):
        arr.array[x] = arr.array[x-1]
    arr.array[index] = new_elt
    return arr

#
# def maybe_extend_array(arr):
#     if (len(arr.array) == arr.size):
#         new_array = ([None] * (round(arr.size * 2)))
#         for i in range(0, arr.size):
#             new_array[i] = arr.array[i]
#         arr.array = new_array
#     return None
