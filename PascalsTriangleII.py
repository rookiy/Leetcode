#!/usr/bin/env python
class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        numRows = rowIndex + 1
        ans = [[1] for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i+1):
                if j < i:
                    x = ans[i-1][j-1] + ans[i-1][j]
                else:
                    x = ans[i-1][j-1]
                ans[i].append(x)
        return ans[rowIndex]

def main():
    import sys
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.getRow(input())
    
if __name__ == '__main__':
    main()

