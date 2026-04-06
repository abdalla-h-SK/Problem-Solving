# 139
# almost figured it out

class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        memo = {}

        def word(i):

            if i in memo:
                return memo[i]
            
            if i == n:
                return True

            for r in range(i + 1, n + 1):
                if s[i:r] in wordDict and word(r):
                    memo[i] = True 
                    return True
            
            memo[i] = False
            return False
        
        return word(0)

# another soluiton -> 

class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]