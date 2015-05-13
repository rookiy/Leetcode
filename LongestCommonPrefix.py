#!/usr/bin/env python
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ''
        ans, flag, length, i = [], True, len(strs[0]), 0
        while flag and i < length:
            current = strs[0][i]
            for tmp in strs:
                if i >= len(tmp) or tmp[i] != current:
                    flag = False
                    break
            if flag:
                ans.append(current)
            i += 1
        return ''.join(ans)
            
