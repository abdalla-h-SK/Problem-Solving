# 172
class Solution(object):
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            x = int(n / 5)
            result += x
            n = x
        return result