#!/usr/bin/env python
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用两个队列，分别保存节点与结果

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        nodelist, resultlist = [root], []
        if not root:
            return resultlist
        while len(nodelist) > 0:
            size, sublist = len(nodelist), []
            for i in range(size):
                node = nodelist.pop(0)
                if node.left:
                    nodelist.append(node.left)
                if node.right:
                    nodelist.append(node.right)
                sublist.append(node.val)
            resultlist.append(sublist)
        return resultlist

def main():
    root = None
    #root = TreeNode(1)
    #root.left = TreeNode(-2)
    #root.right = TreeNode(-3)
    #root.left.left = TreeNode(1)
    #root.left.right = TreeNode(3)
    #root.right.left = TreeNode(-2)
    #root.right.right = TreeNode(-2)
    #root.left.left.left = TreeNode(-1)
    solution = Solution()
    print solution.levelOrder(root)
    
if __name__ == '__main__':
    main()     


            
