# 44
# not the best soluiton ->

class Solution(object):
    def isMatch(self, s, p):
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = (i < len(s)) and (p[j] == s[i] or p[j] == '?')
            second_match = (i < len(s)) and (p[j] == '*')

            if j < len(p) and p[j] == '*':
                res = (dp(i, j + 1) or (second_match and dp(i + 1, j)))
            else:
                res = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)
    
# another solution ->

class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
        return dp[m][n]