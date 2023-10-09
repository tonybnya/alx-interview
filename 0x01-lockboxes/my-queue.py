#!/usr/bin/python3
"""
This helper file implements a queue data structure using a list.
The queue simulates the FIFO concept
"""


class MyQueue:
    """
    Class definition
    """
    def __init__(self):
        """ Initialization. """
        self.queue = []

    def is_empty(self):
        """ Check if the queue is empty. """
        return len(self.queue) == 0

    def push(self, item):
        """ Add an item to the queue. """
        self.queue.append(item)

    def pop(self):
        """ Pop an item to the head of the queue. """
        if self.is_empty():
            return 'Queue is empty'
        return self.queue.pop(0)

    def size(self):
        """ Get the size/length of the queue. """
        return len(self.queue)

    def display(self):
        """ Print output a representation of the queue. """
        if self.is_empty():
            return 'Nothing to print'
        return '<- ' + ' <- '.join([str(num) for num in self.queue]) + ' <-'
