#!/usr/bin/env python
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 使用递归 preorder，遍历每个节点。
class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        self.ans = []
        self.buildResult(root, 0)
        return self.ans
    def buildResult(self, root, level):
        if not root:
            return
        if len(self.ans) == level:
            self.ans.append([])
        self.ans[level].append(root.val)
        self.buildResult(root.left, level+1)
        self.buildResult(root.right, level+1)
 
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
    print solution.levelOrder(root)
    
if __name__ == '__main__':
    main()     

