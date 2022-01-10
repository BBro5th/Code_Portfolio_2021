# Day 7 Exercise

"""
1.      Download the Stack.py file and 07BalancedParentheses.py. Put them into the same project
2.      Currently, Balance only handles parentheses.
        Study the code and try the following inputs with debugger to learn how this program works:
        2*(1+3)
        2*1+3)
        2*(1+3
        We will modify it so that it handles curly braces ({ and }) and square brackets ([ and ]) too.
3.      This requires us to make sure that when we pop off the stack, the popped symbol corresponds with the current symbol being processed.
        Consider the following test cases:
        5+[2*(1+3)]   --> balanced
        5+2*(1+3)]   --> not balanced
        5+{2*(1+3)]   --> not balanced
        5+(2*[1+3)]   --> not balanced
4.      Make sure you can use the debugger in PyCharm to look at the values at any point during the execution.
"""

from Stack import *
text = input("Enter some text and I'll check for balanced parentheses: ")

myStack = Stack()

badInput = False
for ch in text:
    if ch == '(' or ch == '[' or ch == '{':
        myStack.push(ch)
    elif ch == ')' or ch == ']' or ch == '}':
        if myStack.isEmpty():
            badInput = True
            break
        elif myStack.peek() == '(':
            if ch != ')':
                badInput = True
                break
        elif myStack.peek() == '[':
            if ch != ']':
                badInput = True
                break
        elif myStack.peek() == '{':
            if ch != '}':
                badInput = True
                break

        myStack.pop()


if myStack.isEmpty() and not badInput:
    print("The Parenthesis are balanced")
else:
    print("The Parenthesis are not balanced")


