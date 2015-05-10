#!/usr/bin/env python
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        l = []
        while n not in l:
            l.append(n)
            tmp = 0
            while n != 0:
                digit = n%10
                tmp = tmp + digit*digit
                n = n/10
            n = tmp
        if n == 1:
            return True
        else:
            return False
