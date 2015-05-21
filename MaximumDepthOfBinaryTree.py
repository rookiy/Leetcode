#!/usr/bin/env python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def main():
    #root = None
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    #root.left.right = TreeNode(3)
    #root.right.left = TreeNode(-2)
    root.right.right = TreeNode(-2)
    #root.left.left.left = TreeNode(-1)
    root.right.right.left = TreeNode(-1)
    solution = Solution()
    print solution.maxDepth(root)
    
if __name__ == '__main__':
    main()     