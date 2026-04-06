# 198
# my soluiton ->

class Solution(object):
    def rob(self, nums):
        n = len(nums)
        memo = {n-1:0, n-2:0}

        def max_rob(i):
            if i == n-3:
                memo[i] = nums[i+2]
                return memo[i]
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i+2] + max_rob(i+2), nums[i+3] + max_rob(i+3))
            return memo[i]
        
        return max_rob(-2)

# a better solution to absorb the objectives !

class Solution(object):
    def rob(self, nums):
        n = len(nums) 
        if n <= 2:
            return max(nums)
        memo = {0:nums[0], 1:max(nums[0], nums[1])}

        def max_rob(i):
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + max_rob(i-2), max_rob(i-1))
            return memo[i]
        
        return max_rob(n-1)
    

# another solution using constant space ->

class Solution(object):
    def rob(self, nums):
        n = len(nums) 
        if n <= 2:
            return max(nums)

        prev, curr = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            prev, curr = curr, max(prev + nums[i], curr)
            
        return curr

