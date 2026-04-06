# 209
# my solution ->

#   Time : O(n)
#   Space: O(1)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        sub = 0
        output = float('inf')
        for r in range(len(nums)):
            sub += nums[r]

            while sub >= target:
                output = min(output, (r - l + 1))
                sub -= nums[l]
                l += 1

        return 0 if output == float('inf') else output