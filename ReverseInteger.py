#!/usr/bin/env python
import sys
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        import math
        flag = True
        if x < 0:
            flag = False
            x = -1*x
        numList = list(str(x))
        numList.reverse()
        if not flag:
            numList.insert(0, '-')
        ans = int(''.join(numList))
        return ans if ans < math.pow(2, 31)-1 and ans > math.pow(2, 31)*-1 else 0
        
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.reverse(input())
    
if __name__ == '__main__':
    main()

