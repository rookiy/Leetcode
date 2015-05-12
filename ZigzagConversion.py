#!/usr/bin/env python
import sys
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        span = 2 * numRows - 2
        l = [[] for i in range(numRows)]
        for index, char in enumerate(s):
            row = index%span
            if row < numRows:
                l[row].append(char)
            else:
                l[span-row].append(char)
        ans = ''.join([''.join(line) for line in l])
        return ans

def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.convert(raw_input(), 3)
    
if __name__ == '__main__':
    main()