# 55
# my solution ->

# Time : O(n) , Space : O(n)

class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        def jump(curr, i):
            if i == n-1:
                return True
            if curr == 0 and nums[i] == 0:
                return False

            return jump(max(curr, nums[i]) - 1, i + 1)
        
        return jump(nums[0], 0)