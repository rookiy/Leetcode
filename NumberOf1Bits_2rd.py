#!/usr/bin/env python
import sys

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return str(bin(n)).count('1')
    
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.hammingWeight(input())
    
if __name__ == '__main__':
    main()
