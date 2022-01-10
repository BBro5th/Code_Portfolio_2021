# Day 10 Exercise (will be counted as Programing Assignment 5)

"""
Part 2:
Write indexOf(value) which returns the index within the linked list of the first node with that value. (Count indexes from 0)
Return -1 if not found.

Write __str__ method which returns a formatted string of all the values in the doubly linked list

You code should produce the same information as indicated in the comments (it is okay if the format is slightly different)

At the end of this program, make a print statement answering what are the time complexities
of the methods you have added.

"""

class DoublyLinkedNode:
    """ A single node in a doubly-linked list.
        Contains 3 instance variables:
            data: The value stored at the node.
            prev: A pointer to the previous node in the linked list.
            next: A pointer to the next node in the linked list.
    """

    def __init__(self, value):
        """
        Initializes a node by setting its data to value and
        prev and next to None.
        """
        self.data = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """
    The doubly-linked list class has 3 instance variables:
        head: The first node in the list.
        tail: The last node in the list.
        size: How many nodes are in the list.
    """

    def __init__(self):
        """
        The constructor sets head and tail to None and the size to zero.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def addFront(self, value):
        """
        Creates a new node (with data = value) and puts it in the
        front of the list.
        """
        newNode = DoublyLinkedNode(value)
        if (self.size == 0):
            self.head = newNode
            self.tail = newNode
            self.size = 1
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.size += 1

    def addRear(self, value):
        """
        Creates a new node (with data = value) and puts it in the
        rear of the list.
        """
        newNode = DoublyLinkedNode(value)
        if (self.size == 0):
            self.head = newNode
            self.tail = newNode
            self.size = 1
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def removeFront(self):
        """
        Removes the node in the front of the list.
        @return Returns the data in the deleted node.
        """
        value = self.head.data
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None
        self.size -= 1
        return value

    def removeRear(self):
        """
        Removes the node in the rear of the list.
        @return Returns the data in the deleted node.
        """
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None
        self.size -= 1
        return value

    def atIndex(self, index):
        """
        Retrieves the data of the item at index.
        @param index The index of the item to retrieve.
        @return Returns the data of the item.
        """
        count = 0
        temp = self.head
        while count < index:
            count += 1
            temp = temp.next
        return temp.data

    def indexOf(self,value):
        count = int(self.size)-1
        temp = self.tail
        while count >=0:
            if temp.data == value:
                return count
            else:
                temp = temp.prev
                count-=1
        if count == -1:
            return count

    def __str__(self):
        count= int(self.size)-1
        temp = self.head
        S = ""
        while count >=0:
            S+= temp.data
            S+=" "
            temp = temp.next
            count-=1
        return S


my_d_linked_list = DoublyLinkedList()

my_d_linked_list.addRear("B")
my_d_linked_list.addRear("C")
my_d_linked_list.addRear("D")
my_d_linked_list.addFront("A")

print(my_d_linked_list)  # head ----A--B--C--D---- rear
my_d_linked_list.addRear("A")
print(my_d_linked_list)  # head ----A--B--C--D--A---- rear
print(my_d_linked_list.indexOf("A"))  #0
print(my_d_linked_list.indexOf("a"))  #-1

print("The time complexity of indexOf() is: O(n)")
print("The time complexity of __str__() is: O(n)")
