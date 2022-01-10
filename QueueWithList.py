# Day 9 Exercise
"""
Change this file name to QueueWithList.py, keep this file in the same folder to your 09DoubleLinkedListComparison.py.
Do not make any change to this file
"""
__author__ = 'guinnc'
class QueueWithList:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

