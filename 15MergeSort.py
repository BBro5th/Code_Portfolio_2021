# Day 15 exercise

# Add additional code to trace the recursions
# After the recursive calls, in the code of merge sort, there are additional steps to merge the sorted sub-lists
# Add the code, for each recursive round, output: what are the two sub-lists to merge and the merged lists
# The expected output should be:

# merging [54]  and  [26]
# Merged:  [26, 54]
# merging [93]  and  [17]
# Merged:  [17, 93]
# merging [26, 54]  and  [17, 93]
# Merged:  [17, 26, 54, 93]
# merging [77]  and  [31]
# Merged:  [31, 77]
# merging [55]  and  [20]
# Merged:  [20, 55]
# merging [44]  and  [20, 55]
# Merged:  [20, 44, 55]
# merging [31, 77]  and  [20, 44, 55]
# Merged:  [20, 31, 44, 55, 77]
# merging [17, 26, 54, 93]  and  [20, 31, 44, 55, 77]
# Merged:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
# merge sort done: [17, 20, 26, 31, 44, 54, 55, 77, 93]


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        print("merging",lefthalf,"and",righthalf)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        print("merged",alist)
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print("merge sort done:", alist)
