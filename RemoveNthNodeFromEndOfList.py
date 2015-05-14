#!/usr/bin/env python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if head == None:
            return head
        node = ListNode(None)
        node.next = head
        num, p, r = 0, head, node
        while p:
            num += 1
            p = p.next
        for i in range(num - n):
            r = r.next
        r.next = r.next.next
        return node.next
        
