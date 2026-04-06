# 1422
# my solutoin ->

class Solution(object):
    def maxScore(self, s):
        n = len(s)
        cur_one = cur_zero = 0
        zeros, ones = [0] * (n - 1), [0] * (n - 1)

        for i in range(n - 1):
            j = -i-1

            if s[i] == '0':
                cur_zero += 1
            if s[j] == '1':
                cur_one += 1
            
            zeros[i] = cur_zero
            ones[j] = cur_one
        
        ans = 0
        for i in range(n - 1):
            ans = max(ans, ones[i] + zeros[i])
        
        return ans