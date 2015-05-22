# -*- coding:utf-8 -*-

# 从nums1末尾开始合并数组，nums1 nums2分别倒叙访问，如果nums2访问完，则合并完成
# 如果nums1访问完，则将nums2的元素依次放到末尾
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        for idx in range(m+n-1, -1, -1):
            if n <= 0:
                break
            elif m <= 0 or nums1[m-1] < nums2[n-1]:
                n -= 1
                nums1[idx] = nums2[n]
            else:
                m -= 1
                nums1[idx] = nums1[m]