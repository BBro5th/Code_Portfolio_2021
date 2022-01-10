# Day 8 Exercise (will be counted as Programing Assignment 4)
"""
1.      Download and include the Deque class in your project
2.      Read in a string from the user
3.      Define and call a method is_palindrome that returns True if s is a palindrome and False otherwise;
4.      Don't worry about spaces or punctuation yet.
5.      How to do it:
    a.      For every character in the string, add to the end of the deque.
    b.      While the length of the deck is greater than 1,
        i.      Remove the front; remove the end; compare.  If equal, keep going
        ii.      Otherwise return False.
    c.       Return True.
"""

from Deque import *
def is_Palindrome():
    IceKnife = Deque()
    DefLepard = input("type a string plox")
    for i in DefLepard:
        IceKnife.addRear(i)
    ItisPal = True
    while IceKnife.size() >= 2:
        if IceKnife.size == 1:
            print("odd palaindrome")
        elif IceKnife.removeFront() == IceKnife.removeRear():
            continue
        else:
            ItisPal = False
            break
    return(ItisPal)

print(is_Palindrome())