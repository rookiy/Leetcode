#!/usr/bin/env python
import sys
#AC, runtime 46ms
class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        valids = ['()', '{}', "[]"]
        if len(s)%2 == 1:
            return False
        while len(s) != 0:
            o_len = len(s)
            for val in valids:
                s = s.replace(val, '')
            if len(s) == o_len:
                return False
        return True
 
def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.isValid(raw_input())
    
if __name__ == '__main__':
    main()
    
