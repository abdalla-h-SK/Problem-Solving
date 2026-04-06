# 53
# my solution ->
 
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        max_count = float('-inf')
        count = 0

        for i in range(n):
            count += nums[i]
            max_count = max(max_count, count)
            if count < 0:
                count = 0
        
        return max_count