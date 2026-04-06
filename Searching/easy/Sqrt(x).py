# 69
# my solution ->

#   Time : O(log(n)) , Space : O(1)

class Solution(object):
    def mySqrt(self, x):
        if x == 1:
            return 1

        l, r = 1, x
        while l < r:
            m = (l + r) // 2

            if m * m > x:
                r = m
            else:
                l = m + 1
        
        return l - 1