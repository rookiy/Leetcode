#!/usr/bin/env python
import sys

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        l = nums[:]
        size = len(nums)
        for index, item in enumerate(nums):
            l[(index+k)%size] = item
        for index, item in enumerate(l):
            nums[index] = item
        print nums
        
        
        
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    nums = map(int, raw_input().split(','))
    solution.rotate(nums,3)
    
if __name__ == '__main__':
    main()