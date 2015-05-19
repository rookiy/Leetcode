#!/usr/bin/env python
# Definition for a binary tree node.
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
        global stack, visited, total
        stack, visited, total = [], [], 0
        return self.DFS(root, sum)
    def DFS(self, root, goal):
        global stack, total, visited
        if not root:
            return False
        while 1:
            total += root.val
            stack.append(root)
            visited.append(1)
            if not root.left and not root.right:
                if total == goal:
                    return True
            if root.right:
                stack.append(root.right)
                visited.append(0)
            if root.left:
                return self.DFS(root.left, goal)
            else:
                while 1:
                    if len(stack) == 0:
                        return False
                    root = stack.pop()
                    if visited.pop() == 0:
                        break
                    else:
                        total -= root.val
    
        
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    print solution.hasPathSum(root, 3)
    
if __name__ == '__main__':
    main()








