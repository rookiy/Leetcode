#!/usr/bin/env python
class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        size = len(s)
        i, j = 0, size-1
        s = s.lower()
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
            
        return True
