#!/usr/bin/env python
import sys

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        l = []
        while n != 0:
            tmp = n % 26
            if tmp == 0:
                tmp = 26
            l.insert(0, chr(tmp + 64))
            n = (n - tmp) / 26
        return ''.join(l)
        
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.convertToTitle(input())
    
if __name__ == '__main__':
    main()
