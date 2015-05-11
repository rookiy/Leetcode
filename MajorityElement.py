#!/usr/bin/env python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        dict = {}
        size = len(nums)/2
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        for k, v in dict.iteritems():
            if v > size:
                return k
            
