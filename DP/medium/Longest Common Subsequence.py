# 1143
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)

        cache = {}

        def longest(i, j):
            if i == m or j == n:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                result = 1 + longest(i+1, j+1)
            else:
                result = max(longest(i, j+1), longest(i+1, j))

            cache[(i, j)] = result
            return result
        
        return longest(0, 0)
    
    
# same same but different but still same

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]