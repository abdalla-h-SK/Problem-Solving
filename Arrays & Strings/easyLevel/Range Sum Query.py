# 303
# my solution ->
# Time : O(n)
# Space: O(n)

class NumArray(object):

    def __init__(self, nums):
        self.count = 0
        self.sums = [0] * len(nums)

        for i in range(len(nums)):
            self.count += nums[i]
            self.sums[i] = self.count

    def sumRange(self, left, right):
        if left == 0: 
            return self.sums[right]
        else:
            return self.sums[right] - self.sums[left-1]