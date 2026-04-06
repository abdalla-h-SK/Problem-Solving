# 45

class Solution(object):
    def jump(self, nums):
        n = len(nums)
        smallest = 0
        end, far = 0, 0

        for i in range(n-1):
            far = max(far, i + nums[i])

            if i == end:
                end = far
                smallest += 1

        return smallest