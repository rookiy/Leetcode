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
        # 使用栈来模拟先序遍历，一个栈保存访问的节点，一个栈保存当前节点的路径值
        stack, vals, total = [], [], 0
        # 如果栈为空或当前节点为空，已经没有未访问的节点，结束循环
        while len(stack) > 0 or root:
            # 如果当前节点存在，访问它，保存节点及路径值，接着访问节点左孩子
            if root:
                total += root.val
                stack.append(root)
                vals.append(total)
                root = root.left
            # 如果当前要访问的位置为空，则弹出上一个访问的节点，如果为叶子，判断路径值
            # 访问该节点的右孩子，这样完成先序遍历
            else:
                root = stack.pop()
                total = vals.pop()
                if not root.left and not root.right and total == sum:
                    return True
                root = root.right
        # 如果先序遍历访问完成没有返回True，那么就不存在路径值等于sum,返回False
        return False
        
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    print solution.hasPathSum(root, 4)
    
if __name__ == '__main__':
    main()
