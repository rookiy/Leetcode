#!/usr/bin/env python
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 使用迭代。分别访问对称的节点。
class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        queue = [p, q]
        while len(queue) > 0:
            p, q = queue.pop(0), queue.pop(0)
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)
        return True


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

