#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 层次遍历的多种方式：
# 1) 我所使用的两个变量cur,last记录当前访问节点，与当前层的
# 最后一个节点的下一个位置，当cur来到last的位置时，表明当前
# 层次已访问完，深度加1，重置last为目前队列的最后一个位置（即下一层最后）
# 2) 使用一个magic节点当做哨兵，记录当前层的最后一个位置
# 3) 记录当前层的最后一个节点p，当前层访问完后，p修正为p的右孩子，不存在
# 时为左孩子，p肯定不为叶节点，否则无需继续循环。
# 4) 记录每层的节点个数，每次访问一层，子节点进队，高度加1，直到队列为空
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
        stack = [root]
        cur, last, height= 0, 1, 1
        while cur < last:
            node = stack[cur]
            if not node.left and not node.right:
                break
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            cur += 1
            if cur == last:
                last = len(stack)
                height += 1
        return height

def main():
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(-2)
    root.left.left.left = TreeNode(-1)
    solution = Solution()
    print solution.minDepth(root)
    
if __name__ == '__main__':
    main()
   
    
    
    
    