#!/usr/bin/env python
class Solution:
    # @param {string[]} strs
    # @return {string}
    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i = i+1
            else:
                break
        return str1[:i]

    # @return a string                                                                                                                                                          
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        else:
            return reduce(self.lcp,strs)
