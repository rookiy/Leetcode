#!/usr/bin/env python
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        n, e = 10, 10
        while x/n:
            n *= 10
        while n > e:
            if x%n/(n/10) != x%e/(e/10):
                return False
            n /= 10
            e *= 10
        return True
