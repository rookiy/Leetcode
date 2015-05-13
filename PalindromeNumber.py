#!/usr/bin/env python
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        numList = list(str(x))
        length = len(numList)
        i, j = 0, length-1
        while i < j:
            if numList[i] != numList[j]:
                return False
            i += 1 
            j -= 1
        return True
