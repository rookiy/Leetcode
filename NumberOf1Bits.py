#!/usr/bin/env python
import sys

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n != 0:
            if n%2 == 1:
                count += 1
            n /= 2
        return count 
    
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.hammingWeight(input())
    
if __name__ == '__main__':
    main()
