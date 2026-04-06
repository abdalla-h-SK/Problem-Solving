# 1122
# my solution ->

from collections import Counter
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
    
        counter = Counter(arr1)
        ans = []

        for i in arr2:
            ans.extend([i] * counter[i])
            del counter[i]
        
        sorted_keys = sorted(counter.keys())

        for i in sorted_keys:
            ans.extend([i] * counter[i])

        return ans