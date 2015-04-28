#!/usr/bin/env python
import sys

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        self.rot(nums, 0, n-1, k%n)
        print nums
    def rot(self, nums, start, end, k):
        if k == 0:
            return
        rev_k = end - start + 1 - k
        if k == rev_k:
            for i in range(end, end-k, -1):
                nums[i], nums[i-k] = nums[i-k], nums[i]
        elif k < rev_k:
            for i in range(end, end-k, -1):
                nums[i], nums[i-rev_k] = nums[i-rev_k], nums[i]
            self.rot(nums, start+k, end, k)
        elif k > rev_k:
            for i in range(end, end-rev_k, -1):
                nums[i], nums[i-k] = nums[i-k], nums[i]
            self.rot(nums, start, end-rev_k, k-rev_k)    
        
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    nums = map(int, raw_input().split(','))
    solution.rotate(nums, 3)
    
if __name__ == '__main__':
    main()