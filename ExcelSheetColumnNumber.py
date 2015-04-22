#!/usr/bin/env python
import sys

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        colNum = 0
        for char in s:
            colNum *= 26
            colNum += ord(char) - ord('A') + 1
        return colNum



def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.titleToNumber(raw_input())
    
if __name__ == '__main__':
    main()
