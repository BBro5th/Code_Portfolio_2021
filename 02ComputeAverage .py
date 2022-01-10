# Day 2 Exercise (will be counted as Programing Assignment 1)

"""
Read in a file (called “numbers.txt”) of integers.  There will be one integer per line.
1.Print the number of integers read in.
2.Print the average of the integers.  Do not use the built-in sum operator on lists.
3.Find and print the minimum.   Do not assume that the minimum must be less than some fixed integer.  Do not use the built-in min operator on lists.
4.Find and print the maximum.  Do not assume the maximum must be greater than some fixed integer.  Do not use the built-in max operator on lists.
5.Print the median of the numbers.  Do not use that statistics package’s median method. This will require you to sort.
If you read the integers into a Python list, you may use the built-in list sorted or sort method.
Then take the one in the middle.  That’s the median.  But what if there is an even number of values?
What’s the “middle” element?  In that case, take the two nearest the middle and average them.

Here are two examples of computing the median.
2 1 10 3 5        To compute the median, sort:   1 2 3 5 10.  Take the one in the middle.
In this case that’s the value 3.    What is its index?   The length of the list divided by 2.

7 12 23 11     To compute the median, sort: 11 12 17 23.
Since there are an even number of elements, average the two in the middle: (12 + 17)/2 = 14.5.
What are the indices of these two elements?  The length of the list divided by 2, and (length of the list divided by 2) minus 1.

Helpful hint #1: How can Python compute whether a number is even or odd?
Take the number and perform modulo 2 (number % 2).  If the answer is 0, it’s even.  If the answer is 1, it’s odd.

Helpful hint #2: Since the index must be an integer, you have a problem if you take an odd number and divide it by 2 to compute an index.
So, how do make sure you end up with an integer?  Use integer division!  That’s the // operator in Python.
"""

# Please feel free to start from the code blow.
# Note that, the numbers.txt should be in the same folder as
input_numbers = open("numbers.txt", "r")
for line in input_numbers:
    x = int(line)
    print(x)
print("---")
input_numbers.close()
# part 2
"""

"""
input_numbers = open("numbers.txt", "r")
listofnumber = []
Numberof = 0
Summation= 0
for line in input_numbers:
    x = int(line)
    Summation+=x
    Numberof +=1
    listofnumber.append(x)
print (Numberof)
print (listofnumber)
print("Tis thy average",Summation/Numberof)
input_numbers.close()
print("---")
# part 3
input_numbers = open("numbers.txt", "r")
min = 0
for line in input_numbers:
    x = int(line)
    if min==0:
        min=x
    elif min > x:
        min=x
    else:
        continue
print(min)
input_numbers.close()
print("---")
# part 4
max = int(0)
input_numbers = open("numbers.txt", "r")
for line in input_numbers:
    x = int(line)
    if min==0:
        min=x
    elif max < x:
        max = x
    else:
        continue
print (max)
input_numbers.close()
print("---")
# part 5
input_numbers = open("numbers.txt", "r")
ListTwoNumber= []
Ack_Number=0
for line in input_numbers:
    x = int(line)
    Ack_Number += 1
    ListTwoNumber.append(x)
ListTwoNumber.sort()
print(ListTwoNumber)
if Numberof % 2 == 1:
    print("odd")
    Mathma=int(Ack_Number-(Ack_Number//2)-1)
    Midnumber=(Mathma)
    print(Midnumber)
    print(ListTwoNumber [Midnumber])
else:
    print ("even")
    Mathnam= (Ack_Number//2)
    Mathka= (Ack_Number//2)-1
    Mathcha= ((ListTwoNumber[Mathnam])+(ListTwoNumber[Mathka]))/2
    print (Mathcha)