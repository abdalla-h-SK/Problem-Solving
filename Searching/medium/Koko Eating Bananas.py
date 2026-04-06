# 875

from math import ceil
class Solution(object):
    def minEatingSpeed(self, piles, h):
        max_h = max(piles)
        l, r = 1, max_h
        
        def can_finish(m):
            hours = 0
            for p in piles:
                hours += ceil(float(p) / float(m))
                
            return hours <= h

        while l < r:
            m = (l + r) // 2

            if can_finish(m):
                r = m
            else:
                l = m + 1
        
        return l