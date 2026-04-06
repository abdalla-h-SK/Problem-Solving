# 213
# my solution ->

class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n <= 2:
            return max(nums)

        def helper(lst):
            n = len(lst)
            
            dp = [0] * n
            dp[0], dp[1] = lst[0], max([lst[0], lst[1]])

            for i in range(2, n):
                dp[i] = max(dp[i-2] + lst[i], dp[i-1])
            
            return dp[n-1]
        
        return max(helper(nums[:n-1]), helper(nums[1:]))