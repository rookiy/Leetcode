#!/usr/bin/env python
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        length1 = len(nums)
        length2 = len(set(nums))
        return length1 != length2
