# 561
# my solution ->

class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        n = len(nums)
        ans = 0
        
        for i in range(0, n, 2):
            ans += nums[i]

        return ans