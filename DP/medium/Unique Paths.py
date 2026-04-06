# 62
# my solution ->

# Time : O(n) , Space : O(n)

class Solution(object):
    def uniquePaths(self, m, n):
        memo = {(m, n):1}
        def paths(r, c):
            if r > m or c > n:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = paths(r + 1, c) + paths(r, c + 1)
            return memo[(r, c)]
        
        return paths(1, 1)

# my second solution using Tabulation ->

class Solution(object):
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1

        dp = [[0]*n for _ in range(m)]

        for j in range(n):
            dp[0][j] = 1

        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]