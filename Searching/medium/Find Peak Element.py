# 162

# my solution ->

#   Time : O(log(n))
#   Space: O(1)

class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l, r = 1, len(nums) - 2

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m+1] > nums[m]:
                l = m + 1
            elif nums[m-1] > nums[m]:
                r = m - 1
            else:
                if nums[l] > nums[r]:
                    r = m - 1
                else:
                    l = m + 1