#!/usr/bin/env python
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        flag = False
        i = len(digits) - 1
        while not flag:
            if i >= 0:
                digits[i] += 1
            else:
                digits.insert(0, 1)
            if digits[i] == 10:
                digits[i] = 0
                i -= 1
            else:
                flag = True
        return digits
