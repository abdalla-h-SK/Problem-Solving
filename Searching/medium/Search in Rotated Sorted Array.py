# 33
# my solution ->

#   Time : O (log (n))
#   Space: O (1)

class Solution(object):
    def search(self, nums, target):
        
        l = 0
        r = len(nums) - 1 

        while l < r :

            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        p = l
        if target == nums[p]:
            return p
        
        l = 0
        r = p

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        l = p + 1
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1
    
# the same but specified!
class Solution(object):
    def search(self, nums, target):
        
        l = 0
        r = len(nums) - 1 

        while l < r :

            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        p = l

        if p == 0:
            l, r = 0, len(nums) - 1

        elif nums[p - 1] >= target >= nums[0]:
            l, r = 0, p - 1
        else:
            l, r = p, len(nums) - 1
            
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1