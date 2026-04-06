# 169
# my solution ->

from collections import defaultdict, Counter
class Solution(object):
    def majorityElement(self, nums):
        case = len(nums) / 2
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
            if counter[i] > case:
                return i
            
#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def majorityElement(self, nums):
        h = Counter(nums)
        return max(h, key=h.get)
    
# d = {1:4, 2:3}
# print(max(d, key=d.get)) --> 1 because 4 is bigger than 3