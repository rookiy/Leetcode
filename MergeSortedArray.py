#!/usr/bin/env python
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        tmp, i, j, k = [0] * (m + n), 0, 0, 0
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                tmp[k] = nums1[i]
                i += 1
            else:
                tmp[k] = nums2[j]
                j += 1
            k += 1
        while i<m:
            tmp[k] = nums1[i]
            i, k = i+1, k+1
        while j<n:
            tmp[k] = nums2[j]
            j, k = j+1, k+1
        for n in range(n+m):
            nums1[n] = tmp[n]
