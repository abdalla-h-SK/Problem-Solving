# 1283
# my solution ->

from math import ceil

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        n = sum(nums)
        l, r = 1, n
        def divide_sum(divisor):
            sum = 0
            for i in nums:
                sum += ceil(float(i) / divisor)
            
            return True if sum <= threshold else False

        while l < r:
            m = (l + r) // 2
            if divide_sum(m):
                r = m
            else:
                l = m + 1

        return r