# 268
# my solutions ->
class Solution(object):
    def missingNumber(self, nums):
        s = set(nums)
        for i in range(max(nums) + 1):
            if i not in s:
                return i
                
        return max(nums) + 1
    
class Solution(object):
    def missingNumber(self, nums):
        minimum = min(nums)
        numbers = set(nums)

        if minimum != 0:
            return 0

        curr = minimum
        for i in range(len(nums)):
            curr += 1
            if curr not in numbers:
                return curr

# another solution ->

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum_nums = sum(nums)
        sum_range = n * (n + 1) / 2
        ans = sum_range - sum_nums
        
        return ans
        
# another solution ->

class Solution(object):
    def missingNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        for i in range(len(nums)+1):
            res ^= i
        return res