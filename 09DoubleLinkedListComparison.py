# Day 9 Exercise

"""
Show that implementing a Queue using a list is not as efficient as implementing a Queue using a (double) linked list.
How?   Take an implementation of a Queue done with a list (QueueWithList.py).
Time how long it takes to enqueue n items and then dequeue n items.
Take an implementation of a Queue done with a linked list (QueueWithLinkedList.py).
Time how long it takes to enqueue n items and then dequeue n items.
Print out the value of n and the two times.
Put this code in a for  loop that varies n from 10000 to 100000
( you can decide the step size to balance the running time and information you want to present)
Produce a graph.

At the end of this program, make a print statement to explain what you have found from your graph

Submit your program and the graph you have made.


"""
import time
from QueueWithList import *
from QueueWithLinkedList import *
#for n in range(10000,100000):

Britain = QueueWithList()

for n in range(10000,100001,1000):
    start = time.clock()
    while int(Britain.size()) < n:
        Britain.enqueue("item")#make it do it n times
    while Britain.size() != 0:
        Britain.dequeue()
    end = time.clock()
    totalTime = end - start
    print(totalTime)
    #print(n)

#Britain.dequeue()

Sweden = QueueWithLinkedList()
for n in range(10000,100001,1000):
    JStart = time.clock()
    while Sweden.size() < n:
        Sweden.enqueue("item")
    while Sweden.size() != 0:
        Sweden.dequeue()
    Jend = time.clock()
    SmotalTime= Jend - JStart
    print(SmotalTime)
    #print(n)

#print((Britain.size()))
print("Explain what you have found from your graph")
print("using a python list can become less efficient over time, and the Doubled Linked List is more effective then the phython list \n for enqueing and dequeueing.")

print("You can use multiple lines of output if you want to")