#!/usr/bin/env python
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        if s.find('IV') != -1:
            sum -= 2
        if s.find('IX') != -1:
            sum -= 2
        if s.find('XL') != -1:
            sum -= 20
        if s.find('XC') != -1:
            sum -= 20
        if s.find('CD') != -1:
            sum -= 200
        if s.find('CM') != -1:
            sum -= 200
        for char in s:
            sum += d[char]
        return sum
    
def main():
    import sys
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.romanToInt(raw_input())
    
if __name__ == '__main__':
    main()

