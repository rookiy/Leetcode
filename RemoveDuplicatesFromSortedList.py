#!/usr/bin/env python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        p, q = head, head.next
        while q != None:
            if q.val != p.val:
                p = p.next
                p.val = q.val
            q = q.next
        p.next = None
        return head
