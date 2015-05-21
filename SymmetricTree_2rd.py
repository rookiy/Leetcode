#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 使用递归，十分简洁。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.compare(root.left, root.right)
    def compare(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)
    '''
    def isSymmetric(self, root):
        def compare(left, right):
            if not left or not right:
                return left == right
            if left.val != right.val:
                return False
            return compare(left.left, right.right) and compare(left.right, right.left)
        if not root:
            return True
        return compare(root.left, root.right)
    '''
def main():
    #root = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    #root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    #root.left.left.left = TreeNode(-1)
    #root.right.right.left = TreeNode(-1)
    solution = Solution()
    print solution.isSymmetric(root)
    
if __name__ == '__main__':
    main()     
