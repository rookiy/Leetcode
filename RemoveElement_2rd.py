#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 遇到目标元素时，将数组末尾的元素放到当前位置
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        p, n = 0, len(nums)
        while p < n:
            if nums[p] != val:
                p += 1
            else:
                nums[p] = nums[n-1]
                n -= 1
        return p