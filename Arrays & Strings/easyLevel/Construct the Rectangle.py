# 492
# my solution ->

import math
class Solution(object):
    def constructRectangle(self, area):
        for w in range(int(math.sqrt(area)), 0, -1):
            l = int(area / w)
            if l * w == area:
                return [l, w]