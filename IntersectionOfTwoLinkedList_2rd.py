#!/usr/bin/env python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA, lenB = 0, 0
        p, q, r = headA, headB, None
        while p:
            lenA += 1
            p = p.next
        while q:
            lenB += 1
            q = q.next
        for i in range(lenA-lenB):
            headA = headA.next
        for i in range(lenB-lenA):
            headB = headB.next
        while 1:
            if headA == headB:
                r = headA
                break
            headA = headA.next
            headB = headB.next
        return r
