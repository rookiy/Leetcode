#!/usr/bin/env python
class Solution:
    # @param {integer} n
    # @return {integer}
    # This is a Fibonacci number, we can get it from recursive way,
    # with a dict to memorize result. We can also get it like below
    # iterative way. No need a array to store all the subproblem ans,
    # two variable is enough.
    def climbStairs(self, n):
        if n <= 2:
            return n
        ways = [0]*n
        ways[0], ways[1] = 1, 2
        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n-1]
