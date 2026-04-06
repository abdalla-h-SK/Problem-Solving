# 1863
# my solution ->

class Solution(object):
    def subsetXORSum(self, nums):
        n = len(nums)
        self.res = 0

        def backtrack(i, sol):
            if i == n:
                self.res += sol
                return
            
            backtrack(i+1, sol)

            sol ^= nums[i]
            backtrack(i+1, sol)
            sol ^= nums[i]
        
        backtrack(0, 0)
        return self.res