#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 同样只使用了一层递归，但同时返回高度和平衡与否，Python大法好
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        h, b = self.getHB(root)
        return b

    def getHB(self, root):
        if not root:
            return 0, True
        h1, b1 = self.getHB(root.left)
        h2, b2 = self.getHB(root.right)
        h = max(h1, h2) + 1
        b = b1 and b2 and abs(h1-h2) <= 1
        return h, b
