# 26
class Solution(object):
    def removeDuplicates(self, nums):
        j = 0
        for i in range(len(nums)):
            nums[i] = nums[j]

            while nums[j] == nums[i]:
                j += 1
                if j == len(nums):
                    return i + 1
                
    #   Time : O (n)
    #   Space: O (1)