# 322
class Solution(object):
    def coinChange(self, coins, amount):
        coins.sort()
        memo = {0:0}
        def change(bal):
            if bal in memo:
                return memo[bal]
            
            minn = float('inf')
            for coin in coins:
                diff = bal - coin
                if diff < 0:
                    break
                minn = min(minn, 1 + change(diff))
            
            memo[bal] = minn
            return minn

        call = change(amount)
        return call if call != float('inf') else -1
    

# another solution ->

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # because c exists so dp[c] will be = 1 !
        
        return dp[amount] if dp[amount] != float('inf') else -1
