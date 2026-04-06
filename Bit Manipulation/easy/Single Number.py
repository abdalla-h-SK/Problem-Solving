# 136
# my solution ->

# Time : O(n)
# Space: O(1)

class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]
        return ans