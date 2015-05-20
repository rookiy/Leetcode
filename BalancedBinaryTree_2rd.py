#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 只用了一层递归，在计算树高的同时，用一个全局变量记录当前树是否平衡，如果不平衡，结束递归
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
        global flag
        flag = True
        self.height(root)
        return flag       
    def height(self, root):
        global flag
        if flag:
            if not root:
                return 0
            else:
                height_l, height_r = self.height(root.left), self.height(root.right)
                if abs(height_l-height_r) > 1:
                    flag = False
                return 1 + max(height_l, height_r)
        else:
            return 0

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