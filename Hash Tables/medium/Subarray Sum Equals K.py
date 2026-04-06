# 560

# my solution ->

#   Time : O(n)
#   Space: O(n)

from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        seen = defaultdict(int)
        seen[0] = 1

        bal = 0
        ans = 0

        for i in range(len(nums)):
            bal += nums[i]
            ans += seen[bal - k]
            seen[bal] += 1
        
        return ans