#!/usr/bin/env python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        node = ListNode(None)
        ans = node
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                ans.next = l1
                l1, ans = l1.next, ans.next
            else:
                ans.next = l2
                l2, ans = l2.next, ans.next
        while l1 != None:
            ans.next = l1
            l1, ans = l1.next, ans.next
        while l2 != None:
            ans.next = l2
            l2, ans = l2.next, ans.next
        return node.next
