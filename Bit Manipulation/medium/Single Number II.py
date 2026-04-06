# 137
# my solution -> using Counter

from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        counter = Counter(nums)
        return min(counter, key=counter.get)

# another solution using Bit Manipulation ->

class Solution(object):
    def singleNumber(self, nums):
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones