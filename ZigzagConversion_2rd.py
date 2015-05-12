#!/usr/bin/env python
import sys
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        row, step = 0, 1
        l = [[] for i in range(numRows)]
        for char in s:
            l[row].append(char)
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step

        ans = ''.join([''.join(line) for line in l])
        return ans

def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.convert(raw_input(), 3)
    
if __name__ == '__main__':
    main()
