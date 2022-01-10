# Day 8 Exercise (will be counted as Programing Assignment 4)
"""
Below is a implementation of Node and UnorderedList from the text book.
The UnorderedList uses the concept of linked list we have learned today.
Study the code.

Add the following methods to the UnorderedList:
__str__(): returns a string of all the items in the linked list.
append(item): adds item to the tail of the list. This method does not return anything. Assume the item is not already in the list.
pop(): removes the last node in the list and returns its data. Assume the list has at least one item.

The testing code is provided in comments, when you finish implementing a method, you can uncomment the testing code
and execute the code to test your program. The expected output is provided as well.
"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self,newData): #good
        current = self.head
        temp = Node(newData)
        #found = False
        if current == None: #good
            temp.setNext(self.head)
            self.head = temp
        else:
            while current != None:
                if current.getNext == None:
                    current.setNext(temp)
                current = current.getNext()

    def pop(self):
        current = self.head
        previous = None
        if current == None:
            print("there aint nothing left!")
        else:
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def __str__(self):
        current = self.head
        count = 0
        strList = ""
        while current != None:
            count = count + 1
            strList += str(current.getData())
            strList += " - "
            current = current.getNext()
        return "head - " + strList + "end"

mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())  #6
print(mylist.search(93))  #True
print(mylist.search(100))  #False

mylist.add(100)
print(mylist.search(100))  #True
print(mylist.size())  #7

mylist.remove(54)
print(mylist.size())  #6
mylist.remove(93)
print(mylist.size())  #5
mylist.remove(31)
print(mylist.size())  #4
print(mylist.search(93))  #False

# test code for your implementation
print("--"*20)

# Code to test __str__
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist)  #head - 54 - 26 - 93 - 17 - 77 - 31 - end
mylist.remove(26)
print(mylist)  #head - 54 - 93 - 17 - 77 - 31 - end

# Code to test append()
mylist.append("this assgt. hurts me!")
print(mylist)
mylist1 = UnorderedList()
mylist1.append("this assgt. hurts me a lot!")
print(mylist1)  #head - this assgt. hurts me a lot! - end

#Code to test pop()
mylist1.pop()
print(mylist1)  #head - end
#
mylist.pop()
mylist.pop()
print(mylist)  #head - 54 - 93 - 17 - 77 - end
