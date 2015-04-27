#!/usr/bin/env python
import sys
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        l = []
        for i in range(32):
            l.append(str(n%2))
            n /= 2
        ans = int(''.join(l), 2)
        return ans

def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.reverseBits(input())
    
if __name__ == '__main__':
    main()
