# 7
# my solution ->
 
#   Time : O(number of digits) , Space : O(1)
 
class Solution(object):
    def reverse(self, x):
        maxx = (2 ** 31) - 1
        sign = -1 if x < 0 else 1

        x = abs(x)

        ans = 0
        while x != 0:
            pick = x % 10
            x //= 10

            ans += pick
            if ans > maxx:
                return 0
            ans *= 10
        
        ans //= 10
        return sign * ans