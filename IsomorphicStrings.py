#!/usr/bin/env python
import sys
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dict = {}
        for (x, y) in zip(s, t):
            if x in dict:
                if y != dict[x]:
                    return False
            else:
                if y in dict.values():
                    return False
                dict[x] = y
        return True

