#!/usr/bin/env python
import sys
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        count = 0
        List = [1 for i in xrange(n)]
        for i in xrange(2,n):
            if List[i] == 1:
                count += 1
                factor = i
                while factor*i < n:
                    List[factor*i] = 0
                    factor += 1
        return count
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.countPrimes(input())
    
if __name__ == '__main__':
    main()