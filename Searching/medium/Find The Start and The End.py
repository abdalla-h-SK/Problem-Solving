# 34

# my solution ->

#   Time : O(log(n))
#   Space: O(1)

class Solution(object):
    def searchRange(self, nums, target):

        if not nums:
            return [-1, -1]

        i = x = 0
        j = y = len(nums) - 1
        
        while i < j:

            m = (i + j) // 2
            if nums[m] == target:
                j = m
            
            elif nums[m] < target:
                i = m + 1

            else:
                j = m - 1

        while x < y:

            n = (x + y + 1) // 2
            if nums[n] == target:
                x = n
            
            elif nums[n] < target:
                x = n + 1

            else:
                y = n - 1

        if (x==y or i==j) and nums[i] != target:
            return [-1, -1]
        return [i, x]
    
