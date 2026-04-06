# 283
# my solution ->

class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                

class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        i, j = 0, 0
        
        while i < n:
            while j < n and nums[j] != 0:
                j += 1
            
            i = j + 1
            while i < n and nums[i] == 0:
                i += 1

            if i == n or j == n:
                break
            
            nums[i], nums[j] = nums[j], nums[i]


# another solution ->

class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        for num in nums:
            if num != 0:
                nums[l] = num
                l += 1
                
        for i in range(l, len(nums)):
            nums[i] = 0