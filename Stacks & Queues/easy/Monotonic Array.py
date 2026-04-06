# 896
# my solution ->

class Solution(object):
    def isMonotonic(self, nums):
        n = len(nums)
        increase = False
        decrease = False

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                increase = True
            if nums[i] < nums[i-1]:
                decrease = True
            
            if decrease and increase:
                return False
        
        return True