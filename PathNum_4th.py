#!/usr/bin/env python
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        stack, vals = [], []
        stack.append(root)
        vals.append(sum)
        while len(stack) > 0 and root:
            root = stack.pop()
            val = vals.pop()
            if not root.left and not root.right and val == root.val:
                return True
            if root.right:
                stack.append(root.right)
                vals.append(val-root.val)
            if root.left:
                stack.append(root.left)
                vals.append(val-root.val)
        return False
        
def main():
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(-2)
    root.left.left.left = TreeNode(-1)
    solution = Solution()
    print solution.hasPathSum(root, 2)
    
if __name__ == '__main__':
    main()

