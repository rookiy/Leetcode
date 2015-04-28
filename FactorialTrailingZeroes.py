#!/usr/bin/env python
import sys
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        count = 0
        while n:
            n /= 5
            count += n
        return count
        
        
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.trailingZeroes(input())
    
if __name__ == '__main__':
    main()        
