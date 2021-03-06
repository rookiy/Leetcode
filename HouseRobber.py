#!/usr/bin/env python
import sys

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        Earning = nums[:]
        Earning.insert(0, 0)
        for i in range(2, len(Earning)):
            Earning[i] = Earning[i-1] if Earning[i-1] > Earning[i] + Earning[i-2] else Earning[i] + Earning[i-2]
        return Earning[len(nums)]
        
        
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.rob([2,4,3,7,5,6,1])
    
if __name__ == '__main__':
    main()
