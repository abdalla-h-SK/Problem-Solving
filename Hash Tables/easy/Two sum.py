# 1
# my solution ->
#   Time : O(n) , Space : O(n)

class Solution(object):
    def twoSum(self, nums, target):
        s = dict()
        for i in range(len(nums)):
            if target - nums[i] in s:
                return [s[target - nums[i]] , i]
            s[nums[i]] = i