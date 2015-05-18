#!/usr/bin/env python
#!/usr/bin/env python
class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, k):
        res = []
        for i in range(0, k):
            curr = list(res[-1]) if len(res) else []
            for i in range(1, len(curr)):
                curr[i] = res[-1][i - 1] + res[-1][i]
            res.append(curr + [1])
        return res

def main():
    import sys
    sys.stdin = open('./1.txt', 'r')
    solution = Solution()
    print solution.generate(input())
    
if __name__ == '__main__':
    main()

