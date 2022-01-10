# day 14 exercise

"""
The definitions of 3 sorting algorithms are from the textbook, you do not need to make any changes.
Create a function generateRandomList which returns a list of n random integers.

In the main body of your programs, try different n numbers from 1 to 50, then some larger numbers from 100 to 5000.
For each n value, generate a random number list. Use different copies of this random number list to run the sorting algorithms.

Make a visualization to compare which is slowest, and which two tend to be faster.

Submit both your visualization and your code.

Hint: those sorting algorithms will sort a list in place. So, to make fair comparisons, we need to make COPIES
of the random list and do sorting on the copies. The code below provides you a sample:

    my_random_list = generateRandomList(999)
    my_copy = my_random_list.copy()
    bubbleSort(my_copy)

"""

import random
import time

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def generateRandomList(n):
    """
    generate random integers and return them as a list.
    The range of the random integers should between 1 and 1000
    :param n:  the number of random integers in the returned list
    :return: a list of n random integers
    """
    randoList = []
    count = 0
    while count < n:
        ad = random.randint(1,1001)
        randoList.append(ad)
        count += 1
    return randoList
#experiment time
"""""
my_random_list = generateRandomList(25)
my_copy = my_random_list.copy()

TT1 = time.clock()
bubbleSort(my_copy)
TS1 = time.clock()
TimeA = TS1 - TT1
print(TimeA)

TT1 = time.clock()
selectionSort(my_copy)
TS1 = time.clock()
TimeA = TS1 - TT1
print(TimeA)

TT1 = time.clock()
insertionSort(my_copy)
TS1 = time.clock()
TimeA = TS1 - TT1
print(TimeA)

my_random_list = generateRandomList(50)
my_copy = my_random_list.copy()
"""""
for k in range(1,51,5):
    my_random_list = generateRandomList(k)
    my_copy = my_random_list

    TT1 = time.clock()
    bubbleSort(my_copy)
    TS1 = time.clock()
    TimeA = TS1 - TT1
    print(TimeA)

    TT1 = time.clock()
    selectionSort(my_copy)
    TS1 = time.clock()
    TimeA = TS1 - TT1
    print(TimeA)

    TT1 = time.clock()
    insertionSort(my_copy)
    TS1 = time.clock()
    TimeA = TS1 - TT1
    print(TimeA)
    print("---")
print("on ononononon")
for j in range(100,5001,500):
    my_random_list = generateRandomList(j)
    my_copy = my_random_list

    TT1 = time.clock()
    bubbleSort(my_copy)
    TS1 = time.clock()
    TimeA = TS1 - TT1
    print(TimeA)

    TT1 = time.clock()
    selectionSort(my_copy)
    TS1 = time.clock()
    TimeA = TS1 - TT1
    print(TimeA)

    TT1 = time.clock()
    insertionSort(my_copy)
    TS1 = time.clock()
    TimeA = TS1 - TT1
    print(TimeA)
    print("---")
