# Day 12 Exercise  (PA6)

"""
Part 1:
The functions below are a sequential search and a binary search. (The binary search does not have the sorting part.)
We also have defined a list called sizes, from 10 to 1000,000.

Let do a comparison, for each size value, you need to:
1) generate that number of random integer values (from 1 to 1000,0000) in a list
2) run a sequential search of -1 and track the time
3) sort the list using .sort() method
4) run a binary search of -1 on the sorted list, and record the time of sorting and binary search
5) Answer this question with a visualization: if we add the sorting time to the binary search, is binary search still faster
   when searching for only one value in an unsorted list? You can make the visualization with Excel.
6) Submit a visualization and your code.
"""

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

def binSearch(list, target):
    return binSearchHelper(list, target, 0, len(list) - 1)

def binSearchHelper(list, target, left, right):
    if left > right:
        return False

    middle = (left + right)//2
    if list[middle] == target:
        return True
    elif list[middle] > target:
        return binSearchHelper(list, target, left, middle - 1)
    else:
        return binSearchHelper(list, target, middle + 1, right)

import random
import time
list_sizes = [10,100,1000,10000,100000,1000000]
TList = []
while len(TList) < 11:
    TList.append(random.randint(1,1000000))
#print(TList)
ThList = []
while len(ThList) < 101:
    ThList.append(random.randint(1,1000000))
#print(ThList)
THEList = []
while len(THEList) < 1001:
    THEList.append(random.randint(1,1000000))
#print(THEList)
THENList = []
while len(THENList) < 10001:
    THENList.append(random.randint(1,1000000))
#print(THENList)
THENTList = []
while len(THENTList) < 100001:
    THENTList.append(random.randint(1,1000000))
#print(THENTList)
ThenThList = []
while len(ThenThList) < 1000001:
    ThenThList.append(random.randint(1,1000000))
#print(ThenThList)



#sequential times

Star = time.clock()
sequentialSearch(TList,-1)
END = time.clock()
time1 = (END - Star)

Star = time.clock()
sequentialSearch(ThList,-1)
END = time.clock()
time2 = (END - Star)

Star = time.clock()
sequentialSearch(THEList,-1)
END = time.clock()
time3 = (END - Star)

Star = time.clock()
sequentialSearch(THENList,-1)
END = time.clock()
time4 = (END - Star)

Star = time.clock()
sequentialSearch(THENTList,-1)
END = time.clock()
time5 = (END - Star)

Star = time.clock()
sequentialSearch(ThenThList,-1)
END = time.clock()
time6 = (END - Star)

print(time1)
print(time2)
print(time3)
print(time4)
print(time5)
print(time6)
#Binary time
print("---")
Start = time.clock()
TList.sort()
binSearch(TList,-1)
EnDME = time.clock()
print(EnDME-Start)

Start = time.clock()
ThList.sort()
binSearch(ThList,-1)
EnDME = time.clock()
print(EnDME-Start)

Start = time.clock()
THEList.sort()
binSearch(THEList,-1)
EnDME = time.clock()
print(EnDME-Start)

Start = time.clock()
THENList.sort()
binSearch(THENList,-1)
EnDME = time.clock()
print(EnDME-Start)

Start = time.clock()
THENTList.sort()
binSearch(THENTList,-1)
EnDME = time.clock()
print(EnDME-Start)

Start = time.clock()
ThenThList.sort()
binSearch(ThenThList,-1)
EnDME = time.clock()
print(EnDME-Start)

