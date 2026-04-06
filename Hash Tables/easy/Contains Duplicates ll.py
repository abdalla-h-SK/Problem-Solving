# 219
# my solution ->

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        numbers = {}
        for i in range(len(nums)):
            if nums[i] in numbers and abs(numbers[nums[i]] - i) <= k:
                return True
            numbers[nums[i]] = i
        
        return False