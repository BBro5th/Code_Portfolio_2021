# Day 10 Exercise (will be counted as Programing Assignment 5)
"""
Part 1
Write a recursive method to reverse a list. It should return a reversed version of the list sent in as an argument.
Specifically, your method should be called reverse_list.
If alist = [1,2,3,4], then reverse_list(alist) should return [4,3,2,1].
If there are any loops in your program (while, for), then this problem will receive a zero.
Do not use any of the built-in functions like reverse, reversed, or slicing. Just write the method recursively.
"""

def reverse_list(list_to_reverse):
    # Add your code here
    if len(list_to_reverse) <= 1:
        return list_to_reverse
    else:
        return reverse_list(list_to_reverse[1:]) +list_to_reverse[0::-1]


### Code to test your work, do not change:
alist = [1,2,3,4]
print(reverse_list(alist))

alist = [1]
print(reverse_list(alist))

alist = [0]
print(reverse_list(alist))