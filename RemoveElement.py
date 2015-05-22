#!/usr/bin/env python
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        count, i, end = 0, 0, len(nums)
        while i<end:
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
            i += 1
        return count
