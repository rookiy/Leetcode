#!/usr/bin/env python
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 思路应该没有问题，使用层次遍历，每次记录一层的节点，包括空节点，
# 比较一层的节点是否对称，问题在于如果是只有2H个节点，仍然相当于一个满二叉树的效率。超时。
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True
        nodelist = [root]
        while 1:
            size, vallist = len(nodelist), []
            for i in range(size):
                node = nodelist.pop(0)
                if node:
                    vallist.append(node.val)
                    nodelist.append(node.left)
                    nodelist.append(node.right)
                else:
                    vallist.append(None)
                    nodelist.append(None)
                    nodelist.append(None)                
            if vallist[::-1] != vallist:
                return False
            if nodelist == [None]*len(nodelist):
                break
        return True

def main():
    #root = None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    #root.left.left.left = TreeNode(-1)
    #root.right.right.left = TreeNode(-1)
    solution = Solution()
    print solution.isSymmetric(root)
    
if __name__ == '__main__':
    main()     