#!/usr/bin/env python
# Definition for a binary tree node.

# -*- coding:utf-8 -*-

# 这里其他语言会使用一个队列保存节点，一个列表保存结果，Python可以只使用一个。
# 使用cur,last记录访问的当前层，和末尾的位置。访问每层时将节点替换成节点的值。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root:
            return []
        stack, cur, last = [[root]], 0, 1
        while cur < last:
            l = []
            for index in range(len(stack[cur])):
                node = stack[cur][index]
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
                stack[cur][index] = node.val
            if l != []:
                stack.append(l)
                last += 1
            cur += 1
        return stack
                
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
