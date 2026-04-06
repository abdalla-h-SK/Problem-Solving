# 1658
# my solution ->

class Solution(object):
    def minOperations(self, nums, x):
        max_range, target = 0, sum(nums) - x
        l, n = 0, len(nums)
        
        if target == 0:
            return n
        if target < 0:
            return -1
        
        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            
            while cur_sum > target:
                cur_sum -= nums[l]
                l += 1
            
            if cur_sum == target:
                max_range = max(max_range, (i - l + 1))
                cur_sum -= nums[l]
                l += 1
        
        return n - max_range if max_range != 0 else -1