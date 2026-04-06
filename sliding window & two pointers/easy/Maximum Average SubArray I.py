# 643

class Solution(object):
    def findMaxAverage(self, nums, k):
        l = 0
        summ = 0
        for i in range(k):
            summ += nums[i]
        max_avg = float(summ) / float(k)

        for i in range(k, len(nums)):
            summ += nums[i]
            summ -= nums[i - k]

            avg = float(summ) / float(k)
            max_avg = max(max_avg, avg)

        return max_avg