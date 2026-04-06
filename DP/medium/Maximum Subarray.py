# 53
# my solution ->

class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = [float('-inf')]
        def sub(i):
            if i == -1:
                return 0
            ans = max(nums[i], nums[i] + sub(i-1))
            max_sum[0] = max(max_sum[0], ans)
            return ans
        sub(n-1)
        return max_sum[0]