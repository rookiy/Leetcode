#!/usr/bin/env python
import sys

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if not nums:
            return
        k%=len(nums)
        nums.reverse()
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        print nums

    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1  
        
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    nums = map(int, raw_input().split(','))
    solution.rotate(nums, 3)
    
if __name__ == '__main__':
    main()