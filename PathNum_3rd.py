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
        # 递归函数访问每个节点
        if not root:
            return False
        # 从根节点开始
        return self.get(root, sum)
    def get(self, root, sum):
        # 如果当前访问节点为空，返回False
        if not root:
            return False
        # 当前节点存在，且为叶子，且值与剩余路径值相同，返回True
        elif not root.left and not root.right and root.val == sum:
            return True
        # 如果当前节点不为叶子，或值不满足，继续访问当前节点的左右孩子
        if self.get(root.left, sum-root.val) or self.get(root.right, sum-root.val):
            # 如果左右孩子存在满足要求的节点，那么返回True
            return True
        # 如果左右孩子不存在满足要求的节点，返回False
        return False
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    print solution.hasPathSum(root, 5)
    
if __name__ == '__main__':
    main()

