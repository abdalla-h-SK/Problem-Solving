# 746
# Memoization
# my solution ->

class Solution(object):
    def minCostClimbingStairs(self, cost):
        cost.insert(0, 0)
        n = len(cost)
        memo = {n:0, n+1:0}
        def min_cost(i):
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(min_cost(i+2), min_cost(i+1))
            return memo[i]
        return min_cost(0)
    
# the same idea !

class Solution(object):
    def minCostClimbingStairs(self, cost):
        memo = {-1:0, -2:0}
        n = len(cost)
        cost.append(0)
        def min_cost(i):
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(min_cost(i-2),min_cost(i-1))
            return memo[i]
        
        return min_cost(n)
    
                # in the above we put in the dict what we will find in that index \ out braces()   out][out
                #  but in down we put wt we will find after that index \ (in braces)   [in edges]
# another solution ->

class Solution(object):
    def minCostClimbingStairs(self, cost):
        memo = {0:0, 1:0}
        n = len(cost)
        def min_cost(i):
            if i in memo:
                return memo[i]

            memo[i] = min(cost[i-2] + min_cost(i-2), cost[i-1] + min_cost(i-1))
            return memo[i]
        
        return min_cost(n)

# the same idea !

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {n-1:0, n-2:0}

        def min_cost(i):
            if i in memo:
                return memo[i]

            memo[i] = min(cost[i+2] + min_cost(i+2), cost[i+1] + min_cost(i+1))
            return memo[i]
        
        return min_cost(-1)
    

# another solution using Tabulation ->

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[n]
    
# another solution with constant space (bottom up) ->

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        prev, curr = 0, 0

        for i in range(2, n+1):
            prev, curr = curr, min(prev + cost[i-2], curr + cost[i-1])
        
        return curr