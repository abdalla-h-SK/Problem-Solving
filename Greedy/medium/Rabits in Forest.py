# 781
# my solution ->

from math import ceil
from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        counter = Counter(answers)
        ans = 0

        for k, v in counter.items():
            if k == 0:
                ans += v
                continue

            max_group = k + 1
            ans += int(ceil(float(v) / max_group)) * max_group
        
        return ans