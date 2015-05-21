#!/usr/bin/env python
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def depth(self, root):
        if not root:
            return 0;
        left = self.depth(root.left)
        right = self.depth(root.right)
        diff = left-right
        if diff > 1 or diff < -1:
            raise Exception("not balance")
        return left > right and left + 1 or right + 1
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        try:
            self.depth(root)
        except:
            return False
        return True
