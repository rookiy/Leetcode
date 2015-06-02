#!/usr/bin/env python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)

    # @return nothing
    def pop(self):
        val = self.stack.pop()
        if val == self.min[-1]:
            self.min.pop()

    # @return an integer
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    # @return an integer
    def getMin(self):
        return self.min[-1]
