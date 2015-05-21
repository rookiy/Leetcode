#!/usr/bin/env python
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 使用递归。Preorder。
class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def main():
    #root = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    #root.left.right = TreeNode(4)
    #root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    #root.left.left.left = TreeNode(-1)
    #root.right.right.left = TreeNode(-1)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(4)
    #root.right.left = TreeNode(4)
    root2.right.right = TreeNode(3)
    #root.left.left.left = TreeNode(-1)
    #root.right.right.left = TreeNode(-1)
    solution = Solution()
    print solution.isSameTree(root, root2)
    
if __name__ == '__main__':
    main()     

