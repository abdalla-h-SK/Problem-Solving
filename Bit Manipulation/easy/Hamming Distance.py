# 461
# my solution ->

class Solution(object):
    def hammingDistance(self, x, y):
        ans = 0
        for i in range(32):
            bit = x ^ y
            ans += bit & 1

            x >>= 1
            y >>= 1
        
        return ans