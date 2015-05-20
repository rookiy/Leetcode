#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用了嵌套的递归，外层递归返回当前树是否平衡，内层递归计算子树高度

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            if abs(self.height(root.left)-self.height(root.right)) <= 1:
                return True
        return False
    def height(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

def main():
    root = TreeNode(1)
    #root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    #root.left.left = TreeNode(1)
    #root.left.right = TreeNode(3)
    #root.right.left = TreeNode(-2)
    root.right.right = TreeNode(-2)
    #root.left.left.left = TreeNode(-1)
    solution = Solution()
    print solution.isBalanced(root)
    
if __name__ == '__main__':
    main()