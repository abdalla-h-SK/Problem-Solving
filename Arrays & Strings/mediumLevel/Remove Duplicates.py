# 80
    
# my solutions ->

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        j = 2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:  
                nums[j] = nums[i]
                j += 1
                
        return j
    
    #   Time : O(n)
    #   Space: O(1)


# another solution ->

class Solution:
    def removeDuplicates(self, nums):
        j = 1
        count = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        
        return j
    
        # Time: O(n)
        # Space: O(1)