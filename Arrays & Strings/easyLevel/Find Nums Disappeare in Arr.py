# 448
# my soluiton ->

class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        ans = []
        for i in range(n):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(1, n+1):
            if i != nums[i-1]:
                ans.append(i)
        
        return ans