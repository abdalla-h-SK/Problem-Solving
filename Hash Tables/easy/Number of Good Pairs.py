# 1512
# my solution ->
from collections import Counter

class Solution(object):
    def numIdenticalPairs(self, nums):
        counter = Counter(nums)
        pairs = 0
        for num in nums:
            counter[num] -= 1
            pairs += counter[num]
        return pairs