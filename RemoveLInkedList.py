#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        # 增加一个头结点使对第一个节点的操作与其余节点统一起来
        node = ListNode(None)
        node.next = head
        prev, p = node, head
        while p != None:
            if p.val == val:
                prev.next = p.next
            else:
                prev = p
            p = p.next
        return node.next
