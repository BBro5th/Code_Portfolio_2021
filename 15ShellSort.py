# Day 15 exercise

# Add additional code to trace the shell sort
# Before each gap insertion sort, output the gap, start and list
# After each gap insertion sort, output the list

# expected output:
# sorting with gap =  4 start index =  0
# list before gap insertion sort: [54, 26, 93, 17, 77, 31, 44, 55, 20]
# list after gap insertion sort: [20, 26, 93, 17, 54, 31, 44, 55, 77]
# --------------------
# sorting with gap =  4 start index =  1
# list before gap insertion sort: [20, 26, 93, 17, 54, 31, 44, 55, 77]
# list after gap insertion sort: [20, 26, 93, 17, 54, 31, 44, 55, 77]
# --------------------
# sorting with gap =  4 start index =  2
# list before gap insertion sort: [20, 26, 93, 17, 54, 31, 44, 55, 77]
# list after gap insertion sort: [20, 26, 44, 17, 54, 31, 93, 55, 77]
# --------------------
# sorting with gap =  4 start index =  3
# list before gap insertion sort: [20, 26, 44, 17, 54, 31, 93, 55, 77]
# list after gap insertion sort: [20, 26, 44, 17, 54, 31, 93, 55, 77]
# --------------------
# sorting with gap =  2 start index =  0
# list before gap insertion sort: [20, 26, 44, 17, 54, 31, 93, 55, 77]
# list after gap insertion sort: [20, 26, 44, 17, 54, 31, 77, 55, 93]
# --------------------
# sorting with gap =  2 start index =  1
# list before gap insertion sort: [20, 26, 44, 17, 54, 31, 77, 55, 93]
# list after gap insertion sort: [20, 17, 44, 26, 54, 31, 77, 55, 93]
# --------------------
# sorting with gap =  1 start index =  0
# list before gap insertion sort: [20, 17, 44, 26, 54, 31, 77, 55, 93]
# list after gap insertion sort: [17, 20, 26, 31, 44, 54, 55, 77, 93]
# --------------------
# [17, 20, 26, 31, 44, 54, 55, 77, 93]

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        #print ("ahaha") ,half of the amount of go through
        for startposition in range(sublistcount):
            print("sorting with gap =",sublistcount,"start index =",startposition )
            print(alist)
            gapInsertionSort(alist,startposition,sublistcount)
            print(alist)
            print("---")
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
