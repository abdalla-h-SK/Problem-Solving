# 120
# my solution ->

class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == n:
                return 0
            
            memo[(i, j)] = min(triangle[i][j] + dp(i+1, j), triangle[i][j] + dp(i+1, j+1))
            return memo[(i, j)]

        return dp(0, 0)