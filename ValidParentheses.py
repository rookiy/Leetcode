#!/usr/bin/env python
import sys
# AC, runtime 57ms
class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) > 0:
                    top = stack.pop()
                else:
                    return False
                if i == ')' and top == '(':
                    continue
                elif i == '}' and top == '{':
                    continue
                elif i == ']' and top == '[':
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
 
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.isValid(raw_input())
    
if __name__ == '__main__':
    main()
    
