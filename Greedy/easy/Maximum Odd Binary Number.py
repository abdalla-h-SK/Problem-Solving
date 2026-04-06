# 2864
# my solution ->

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        n = len(s)
        ones = -1

        for i in s:
            if i == '1':
                ones += 1

        
        ans = ['0'] * n
        ans[n - 1] = '1'

        i = 0
        while ones:
            ans[i] = '1'
            ones -= 1

            i += 1
        
        return ''.join(ans)