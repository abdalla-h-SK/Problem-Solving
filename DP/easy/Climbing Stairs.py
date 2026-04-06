# 70
# memoization ->
class Solution(object):
    def climbStairs(self, n):
        memo = {1:1, 2:2}
        def fib(n):
            if n in memo:
                return memo[n]
            
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
        return fib(n)

# another solution -> Tabulation !(mine)

class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]