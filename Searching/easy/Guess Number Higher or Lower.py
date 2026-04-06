# 374
# my solution ->

def guess(num):
    pass

class Solution(object):
    def guessNumber(self, n):
        l, r = 1, n
        while l <= r:
            m = (l +r) // 2
            signal = guess(m)

            if signal == -1:
                r = m - 1
            elif signal == 1:
                l = m + 1
            else:
                return m