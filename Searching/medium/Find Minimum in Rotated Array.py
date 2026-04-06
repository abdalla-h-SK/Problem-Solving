# 153
# my solution ->

#   Time : O(log (n))
#   Space: O(1)

class Solution(object):
    def findMin(self, nums):
        if nums[0] < nums[-1]:
            return nums[0]
            
        l = 0
        r = len(nums) - 1
        check = nums[0]

        while l < r :

            m = (l + r) // 2

            if nums[m] < check:
                r = m
            else:
                l = m + 1
        
        return nums[l]
    

# another solution ->

#   Time : O(log (n))
#   Space: O(1)

class Solution(object):
    def findMin(self, nums):

        l = 0
        r = len(nums) - 1

        while l < r :

            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[l]