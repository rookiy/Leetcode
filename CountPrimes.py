#!/usr/bin/env python
import sys
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0
        count = 1
        for i in range(3, n, 2):
            if self.isPrime(i):
                count += 1
        return count
    def isPrime(self, num):
        import math
        boundary = int(math.sqrt(num)) + 1
        for i in range(2, boundary):
            if num%i == 0:
                return False
        return True

def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.countPrimes(input())
    
if __name__ == '__main__':
    main()