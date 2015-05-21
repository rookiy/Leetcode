#!/usr/bin/env python

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 使用迭代。分别访问对称的节点。
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True
        queue_l, queue_r = [root.left], [root.right]
        while len(queue_l)>0 and len(queue_r)>0:
            left, right = queue_l.pop(0), queue_r.pop(0)
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue_l.append(left.left)
            queue_l.append(left.right)
            queue_r.append(right.right)
            queue_r.append(right.left)
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
    solution = Solution()
    print solution.isSymmetric(root)
    
if __name__ == '__main__':
    main()     
