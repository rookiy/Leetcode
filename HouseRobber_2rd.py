#!/usr/bin/env python
#!/usr/bin/env python
import sys
import math
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        a, b = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                a = a + nums[i] if a + nums[i] > b else b
            else:
                b = b + nums[i] if b + nums[i] > a else a
        return a if a>b else b
        
        
        
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.rob([2,4,3,7,5,6,1])
    
if __name__ == '__main__':
    main()

