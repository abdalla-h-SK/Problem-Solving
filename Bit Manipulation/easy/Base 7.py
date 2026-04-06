# 504
# my solution ->

# Tiem : O(log(n))
# Space: O(1)

class Solution(object):
    def convertToBase7(self, num):
        neg = True if num < 0 else False
        num = abs(num)

        if num == 0:
            return '0'
        
        ans = ''
        while num != 0:
            num, mod = num // 7, num % 7
            ans += str(mod)

        return '-'+ans[::-1] if neg else ans[::-1]