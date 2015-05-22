#!/usr/bin/env python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, pre = 1, nums[0]
        while i < len(nums):
            if pre == nums[i]:
                nums.pop(i)
            else:
                pre = nums[i]
                i += 1
        return i
