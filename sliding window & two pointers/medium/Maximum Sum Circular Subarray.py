# 918
# my solution ->

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        n = len(nums)
        max_right = [float('-inf')] * n
        ans = right = nums[-1]

        for i in range(n-2, -1, -1):
            ans = max(ans, nums[i])

            max_right[i] = max(max_right[i + 1], right)
            right += nums[i]

        max_right[-1] = 0
        

        all_left, left, max_left = 0, 0, float('-inf')
        for i in range(n):
            all_left += nums[i]

            left += nums[i]
            max_left = max(max_left, left)
    
            ans = max(ans, max_left, (all_left + max_right[i]))

            if left < 0:
                left = 0
        
        return ans