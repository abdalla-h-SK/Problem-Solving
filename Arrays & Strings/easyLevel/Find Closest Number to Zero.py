# 2239

#   Time: O(n)
#   Space:O(n)

class Solution(object):
    def findClosestNumber(self, nums):
        s = set(nums)
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i
        
        if closest < 0 and abs(closest) in s:
            return abs(closest)
        else:
            return closest