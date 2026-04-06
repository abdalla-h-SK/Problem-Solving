# 64
# my solution ->

class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        memo = {}

        def dp(i=0, j=0):
            if (i, j) in memo:
                return memo[(i, j)]
                
            if (i < m - 1 and j == n) or (i == m and j < n - 1):
                return float('inf')
            
            if i == m or j == n:
                return 0

            memo[(i, j)] = min(grid[i][j] + dp(i+1, j), grid[i][j] + dp(i, j+1))
            return memo[(i, j)]
        
        return dp()


# another solution -> Tabluation is always better! You just can extract it from Tob Down solution ^

class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]