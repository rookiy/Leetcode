#!/usr/bin/env python
import sys

class Solution:
    # @param n, an integer
    # @return a string
    def countAndSay(self, n):
        n_list = ['1']
        for i in range(n-1):
            tmp = []
            count = 1
            char = n_list[0]
            N = len(n_list)
            for j in range(1,N):
                if n_list[j] == char:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(char)
                    count = 1
                    char = n_list[j]
            if count != 0:
                tmp.append(str(count))
                tmp.append(char)
            n_list = tmp
        return ''.join(n_list)
        

def main():
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.countAndSay(input())
    
if __name__ == '__main__':
    main()
