#!/usr/bin/env python
import sys
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        length = len(s)
        for i in range(length):
            if i+1 < length and d[s[i+1]]>d[s[i]]:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
        return ans

def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.romanToInt(raw_input())
    
if __name__ == '__main__':
    main()
