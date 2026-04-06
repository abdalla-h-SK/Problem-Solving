# 1207

# Time : O(n)
# Space: O(n)

from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        counter = Counter(arr)
        s = set()
        for occ in counter.values():
            if occ in s:
                return False
            s.add(occ)
        return True