# 1679
# my solution ->

class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0

        while l < r:
            num = nums[l] + nums[r]
            if num == k:
                ans += 1
                l += 1
                r -= 1
            elif num > k:
                r -= 1
            else:
                l += 1
        
        return ans