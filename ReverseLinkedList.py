#!/usr/bin/env python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        r = None
        # here is a interesting fact, code below is wrong
        # Runtime Error Message: Line 17: AttributeError: 'NoneType' object has no attribute 'next'
        # Last executed input:	[1]
        # while head != None:
        # head, head.next, r = head.next, r, head
        # however, version here can AC
        while head != None:
            head.next, r, head = r, head, head.next
        return r

def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    nums = map(int, raw_input().split(','))
    solution.rotate(nums, 3)
    
if __name__ == '__main__':
    main()
