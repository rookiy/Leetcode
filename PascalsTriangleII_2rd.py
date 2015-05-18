#!/usr/bin/env python
class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, k):
        res = []
        for i in range(0, k + 1):
            for j in reversed(range(1, len(res))):
                res[j] += res[j - 1]
            res += [1]
        return res

def main():
    import sys
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.getRow(input())
    
if __name__ == '__main__':
    main()
