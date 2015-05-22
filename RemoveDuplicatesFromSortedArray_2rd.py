#!/usr/bin/env python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, j, end = 0, 1, len(nums)
        while j < end:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
    
def main():
    solution = Solution()
    print solution.removeDuplicates([1,1,1,2,2,2])
    
if __name__ == '__main__':
    main(
        
    )
                
